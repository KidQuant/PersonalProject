import matplotlib.pyplot as plt
import numpy as np
import quantecon as qe
import random

from numba import jit, jitclass, int64, float64

arellano_data = [
    ('B', float64[:]), ('P', float64[:, :]), ('y', float64[:]),
    ('β', float64), ('γ', float64), ('r', float64),
    ('ρ', float64), ('η', float64), ('θ', float64),
    ('def_y', float64[:])
]

# Defien utility function
# Define utility function


@jit(nopython=True)
def u(c, γ):
    return c**(1 - γ) / (1 - γ)


@jitclass(arellano_data)
class Arellano_Economy:
    """
    Arellano 2008 deals with a small open economy whose government
    invests in foreign assets in order to smooth the consumption of
    domestic households. Domestic households receive a stochastic
    path of income.

    Parameters
    ----------
    B : vector(float64)
        A grid for bond holdings
    P : matrix(float64)
        The transition matrix for a country's output
    y : vector(float64)
        The possible output states
    β : float
        Time discounting parameter
    γ : float
        Risk-aversion parameter
    r : float
        int lending rate
    ρ : float
        Persistence in the income process
    η : float
        Standard deviation of the income process
    θ : float
        Probability of re-entering financial markets in each period
    """

    def __init__(
        self, B, P, y,
        β=0.953, γ=2.0, r=0.017,
        ρ=0.945, η=0.025, θ=0.282
    ):

        # Save parameters
        self.B, self.P, self.y = B, P, y
        self.β, self.γ, self.r, = β, γ, r
        self.ρ, self.η, self.θ = ρ, η, θ

        # Compute the mean output
        self.def_y = np.minimum(0.969 * np.mean(y), y)

    def bellman_default(self, iy, EVd, EV):
        """
        The RHS of the Bellman equation when the country is in a
        defaulted state on their debt
        """
        # Unpack certain parameters for simplification
        β, γ, θ = self.β, self.γ, self.θ

        # Compute continuation value
        zero_ind = len(self.B) // 2
        cont_value = θ * EV[iy, zero_ind] + (1 - θ) * EVd[iy]

        return u(self.def_y[iy], γ) + β * cont_value

    def bellman_nondefault(self, iy, iB, q, EV, iB_tp1_star=-1):
        """
        The RHS of the Bellman equation when the country is not in a
        defaulted state on their debt
        """
        # Unpack certain parameters for simplification
        β, γ, θ = self.β, self.γ, self.θ
        B, y = self.B, self.y

        # Compute the RHS of Bellman equation
        if iB_tp1_star < 0:
            iB_tp1_star = self.compute_savings_policy(iy, iB, q, EV)
        c = max(y[iy] - q[iy, iB_tp1_star] * B[iB_tp1_star] + B[iB], 1e-14)

        return u(c, γ) + β * EV[iy, iB_tp1_star]

    def compute_savings_policy(self, iy, iB, q, EV):
        """
        Finds the debt/savings that maximizes the value function
        for a particular state given prices and a value function
        """
        # Unpack certain parameters for simplification
        β, γ, θ = self.β, self.γ, self.θ
        B, y = self.B, self.y

        # Compute the RHS of Bellman equation
        current_max = -1e14
        iB_tp1_star = 0
        for iB_tp1, B_tp1 in enumerate(B):
            c = max(y[iy] - q[iy, iB_tp1] * B[iB_tp1] + B[iB], 1e-14)
            m = u(c, γ) + β * EV[iy, iB_tp1]

            if m > current_max:
                iB_tp1_star = iB_tp1
                current_max = m

        return iB_tp1_star


@jit(nopython=True)
def solve(model, tol=1e-8, maxiter=10_000):
    """
    Given an Arellano_Economy type, this function computes the optimal
    policy and value functions
    """
    # Unpack certain parameters for simplification
    β, γ, r, θ = model.β, model.γ, model.r, model.θ
    B = np.ascontiguousarray(model.B)
    P, y = np.ascontiguousarray(model.P), np.ascontiguousarray(model.y)
    nB, ny = B.size, y.size

    # Allocate space
    iBstar = np.zeros((ny, nB), int64)
    default_prob = np.zeros((ny, nB))
    default_states = np.zeros((ny, nB))
    q = np.ones((ny, nB)) * 0.95
    Vd = np.zeros(ny)
    Vc, V, Vupd = np.zeros((ny, nB)), np.zeros((ny, nB)), np.zeros((ny, nB))

    it = 0
    dist = 10.0
    while (it < maxiter) and (dist > tol):

        # Compute expectations used for this iteration
        EV = P @ V
        EVd = P @ Vd

        for iy in range(ny):
            # Update value function for default state
            Vd[iy] = model.bellman_default(iy, EVd, EV)

            for iB in range(nB):
                # Update value function for non-default state
                iBstar[iy, iB] = model.compute_savings_policy(iy, iB, q, EV)
                Vc[iy, iB] = model.bellman_nondefault(
                    iy, iB, q, EV, iBstar[iy, iB])

        # Once value functions are updated, can combine them to get
        # the full value function
        Vd_compat = np.reshape(np.repeat(Vd, nB), (ny, nB))
        Vupd[:, :] = np.maximum(Vc, Vd_compat)

        # Can also compute default states and update prices
        default_states[:, :] = 1.0 * (Vd_compat > Vc)
        default_prob[:, :] = P @ default_states
        q[:, :] = (1 - default_prob) / (1 + r)

        # Check tolerance etc...
        dist = np.max(np.abs(Vupd - V))
        V[:, :] = Vupd[:, :]
        it += 1

    return V, Vc, Vd, iBstar, default_prob, default_states, q


def simulate(model, T, default_states, iBstar, q, y_init=None, B_init=None):
    """
    Simulates the Arellano 2008 model of sovereign debt

    Parameters
    ----------
    model: Arellano_Economy
        An instance of the Arellano model with the corresponding parameters
    T: integer
        The number of periods that the model should be simulated
    default_states: array(float64, 2)
        A matrix of 0s and 1s that denotes whether the country was in
        default on their debt in that period (default = 1)
    iBstar: array(float64, 2)
        A matrix which specifies the debt/savings level that a country holds
        during a given state
    q: array(float64, 2)
        A matrix that specifies the price at which a country can borrow/save
        for a given state
    y_init: integer
        Specifies which state the income process should start in
    B_init: integer
        Specifies which state the debt/savings state should start

    Returns
    -------
    y_sim: array(float64, 1)
        A simulation of the country's income
    B_sim: array(float64, 1)
        A simulation of the country's debt/savings
    q_sim: array(float64, 1)
        A simulation of the price required to have an extra unit of
        consumption in the following period
    default_sim: array(bool, 1)
        A simulation of whether the country was in default or not
    """
    # Find index i such that Bgrid[i] is approximately 0
    zero_B_index = np.searchsorted(model.B, 0.0)

    # Set initial conditions
    in_default = False
    max_y_default = 0.969 * np.mean(model.y)
    if y_init == None:
        y_init = np.searchsorted(model.y, model.y.mean())
    if B_init == None:
        B_init = zero_B_index

    # Create Markov chain and simulate income process
    mc = qe.MarkovChain(model.P, model.y)
    y_sim_indices = mc.simulate_indices(T + 1, init=y_init)

    # Allocate memory for remaining outputs
    Bi = B_init
    B_sim = np.empty(T)
    y_sim = np.empty(T)
    q_sim = np.empty(T)
    default_sim = np.empty(T, dtype=bool)

    # Perform simulation
    for t in range(T):
        yi = y_sim_indices[t]

        # Fill y/B for today
        if not in_default:
            y_sim[t] = model.y[yi]
        else:
            y_sim[t] = np.minimum(model.y[yi], max_y_default)
        B_sim[t] = model.B[Bi]
        default_sim[t] = in_default

        # Check whether in default and branch depending on that state
        if not in_default:
            if default_states[yi, Bi] > 1e-4:
                in_default = True
                Bi_next = zero_B_index
            else:
                Bi_next = iBstar[yi, Bi]
        else:
            Bi_next = zero_B_index
            if np.random.rand() < model.θ:
                in_default = False

        # Fill in states
        q_sim[t] = q[yi, Bi_next]
        Bi = Bi_next

    return y_sim, B_sim, q_sim, default_sim


β, γ, r = 0.953, 2.0, 0.017
ρ, η, θ = 0.945, 0.025, 0.282
ny = 21
nB = 251
Bgrid = np.linspace(-0.45, 0.45, nB)
mc = qe.markov.tauchen(ρ, η, 0, 3, ny)
ygrid, P = np.exp(mc.state_values), mc.P

ae = Arellano_Economy(
    Bgrid, P, ygrid, β=β, γ=γ, r=r, ρ=ρ, η=η, θ=θ
)

V, Vc, Vd, iBstar, default_prob, default_states, q = solve(ae)


# Create "Y High" and "Y Low" values as 5% devs from mean
high, low = np.mean(ae.y) * 1.05, np.mean(ae.y) * .95
iy_high, iy_low = (np.searchsorted(ae.y, x) for x in (high, low))

fig, ax = plt.subplots(figsize=(10, 6.5))
ax.set_title("Bond price schedule $q(y, B')$")

# Extract a suitable plot grid
x = []
q_low = []
q_high = []
for i in range(nB):
    b = ae.B[i]
    if -0.35 <= b <= 0:  # To match fig 3 of Arellano
        x.append(b)
        q_low.append(q[iy_low, i])
        q_high.append(q[iy_high, i])
ax.plot(x, q_high, label="$y_H$", lw=2, alpha=0.7)
ax.plot(x, q_low, label="$y_L$", lw=2, alpha=0.7)
ax.set_xlabel("$B'$")
ax.legend(loc='upper left', frameon=False)
plt.show()

# Create "Y High" and "Y Low" values as 5% devs from mean
high, low = np.mean(ae.y) * 1.05, np.mean(ae.y) * .95
iy_high, iy_low = (np.searchsorted(ae.y, x) for x in (high, low))

fig, ax = plt.subplots(figsize=(10, 6.5))
ax.set_title("Value Functions")
ax.plot(ae.B, V[iy_high], label="$y_H$", lw=2, alpha=0.7)
ax.plot(ae.B, V[iy_low], label="$y_L$", lw=2, alpha=0.7)
ax.legend(loc='upper left')
ax.set(xlabel="$B$", ylabel="$V(y, B)$")
ax.set_xlim(ae.B.min(), ae.B.max())
plt.show()

xx, yy = ae.B, ae.y
zz = default_prob

# Create figure
fig, ax = plt.subplots(figsize=(10, 6.5))
hm = ax.pcolormesh(xx, yy, zz)
cax = fig.add_axes([.92, .1, .02, .8])
fig.colorbar(hm, cax=cax)
ax.axis([xx.min(), 0.05, yy.min(), yy.max()])
ax.set(xlabel="$B'$", ylabel="$y$", title="Probability of Default")
plt.show()

T = 250

np.random.seed(42)
y_vec, B_vec, q_vec, default_vec = simulate(ae, T, default_states, iBstar, q)

# Pick up default start and end dates
start_end_pairs = []
i = 0
while i < len(default_vec):
    if default_vec[i] == 0:
        i += 1
    else:
        # If we get to here we're in default
        start_default = i
        while i < len(default_vec) and default_vec[i] == 1:
            i += 1
        end_default = i - 1
        start_end_pairs.append((start_default, end_default))

plot_series = (y_vec, B_vec, q_vec)
titles = 'output', 'foreign assets', 'bond price'

fig, axes = plt.subplots(len(plot_series), 1, figsize=(10, 12))
fig.subplots_adjust(hspace=0.3)

for ax, series, title in zip(axes, plot_series, titles):
    # Determine suitable y limits
    s_max, s_min = max(series), min(series)
    s_range = s_max - s_min
    y_max = s_max + s_range * 0.1
    y_min = s_min - s_range * 0.1
    ax.set_ylim(y_min, y_max)
    for pair in start_end_pairs:
        ax.fill_between(pair, (y_min, y_min), (y_max, y_max),
                        color='k', alpha=0.3)
    ax.grid()
    ax.plot(range(T), series, lw=2, alpha=0.7)
    ax.set(title=title, xlabel="time")

plt.show()

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import numpy as np
import pandas as pd
import requests

import os
import json
from copy import deepcopy

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
logging.getLogger("requests").setLevel(logging.ERROR) # silencing requests logging

# Logging for this notebook
logger = logging.getLogger()
logger.setLevel(logging.INFO) # set this to whatever you'd like


BASE_URL = 'http://api.open.fec.gov/v1'

API_KEY = 'DOACtjrmjEA6B0qvpYE1rDtmrTQvlOo9EGKzjCJV'

def all_results(endpoint, params):
    _params = deepcopy(params)
    _params.update({'api_key': API_KEY})
    _url = BASE_URL+endpoint
    logging.info('querying endpoint: {}'.format(_url))

    initial_resp = requests.get(_url, params=_params)

    logging.debug('full url eg: {}'.format(initial_resp.url))

    initial_data = initial_resp.json()

    num_pages = initial_data['pagination']['pages']
    num_records = initial_data['pagination']['count']
    logging.info('{p} pages to be retrieved, with {n} records'.format(
            p=num_pages, n=num_records))

    current_page = initial_data['pagination']['page']
    logging.debug('page {} retrieved'.format(current_page))

    for record in initial_data['results']:
        yield record

    while current_page < num_pages:
        current_page += 1
        _params.update({'page': current_page})
        _data = requests.get(_url, params=_params).json()
        logging.debug('page {} retrieved'.format(current_page))
        for record in _data['results']:
            yield record

    logging.info('all pages retrieved')

def count_results(endpoint, params):
    _params = deepcopy(params)
    _params.update({'api_key': API_KEY})
    _url = BASE_URL+endpoint

    _data = requests.get(_url, params=_params).json()

    return _data['pagination']['count']



q_all_2024_present_prez_candidates = {
    "cycle": 2024,
    "office": "P",
}

count_results('/candidates', q_all_2024_present_prez_candidates)

prez_candidates_2024 = [c for c in all_results('/candidates',
                                               q_all_2024_present_prez_candidates)]
prez_candidates_2024_df = pd.DataFrame(prez_candidates_2024)

prez_candidates_2024_df[['name','party','candidate_id']].sort_values('name')[370:390]

prez_candidates_2024_df[prez_candidates_2024_df['name'].str.contains('DESANTIS')]

candidates_to_focus_on = ['TRUMP, DONALD J.',
                            'DESANTIS, RON']

candidate_filter = prez_candidates_2024_df.name.str.match(
    '|'.join(candidates_to_focus_on), case=False)

prez_candidates_2024_df[candidate_filter].T

q_my_2024_prez_candidates = {
    "cycle": 2024,
    "incumbent_challenge": "C",
    "office": "P",
    "candidate_id": ['P40013039', 'P80001571']
}

my_2024_prez_candidates = [c for c in all_results('/candidates', q_my_2024_prez_candidates)]
my_2024_prez_candidates_df = pd.DataFrame(my_2024_prez_candidates)
my_2024_prez_candidates_df.T

[r for r in all_results('/candidate/P40013039',{})]

[r['name'] for r in all_results('/candidate/P40013039/committees',{'cycle':2024})]


[(r['designation_full'],r['committee_type_full']) for r in all_results('/candidate/P40013039/committees',{'cycle':2024})]

[r for r in all_results('/candidate/P40013039/committees', {'cycle':2024, 'designation': 'P', 'committee_type': 'P'})]

my_2024_prez_committees = []

for i, row in my_2024_prez_candidates_df.iterrows():
    endpoint = '/candidate/{c}/committees'.format(c=row.candidate_id)
    for res in all_results(endpoint, {'cycle':2024,
                                      'designation': 'P',
                                      'committee_type': 'P'}):
        res['candidate_id'] = row.candidate_id
        my_2024_prez_committees.append(res)

my_2024_prez_committees_df = pd.DataFrame(my_2024_prez_committees)
my_2024_prez_committees_df[['name','committee_id','candidate_id']]

my_2024_prez_committee_totals = []

for i, row in my_2024_prez_committees_df.iterrows():
    endpoint = '/committee/{c}/totals'.format(c=row.committee_id)
    for res in all_results(endpoint, {'cycle':2024}):
        my_2024_prez_committee_totals.append(res)

my_2024_prez_committee_totals_df = pd.DataFrame(my_2024_prez_committee_totals)
my_2024_prez_committee_totals_df[['committee_id','contributions','disbursements','receipts',]]

my_2024_prez_candidates_df.columns

comparison = my_2024_prez_committees_df.set_index('committee_id').join(
                my_2024_prez_committee_totals_df.set_index('committee_id'), rsuffix='.cmte')

comparison = comparison.set_index('candidate_id').join(
                my_2024_prez_candidates_df.set_index('candidate_id'), rsuffix='.cand')

comparison.set_index('name.cand')[['disbursements','receipts',]].plot(kind='barh')

[c for c in comparison.columns]

comparison.set_index('name.cand')[
    ['individual_itemized_contributions',
     'individual_unitemized_contributions',
     'transfers_from_affiliated_committee',
     'other_political_committee_contributions',
     'candidate_contribution',
     'other_loans_received',
     'offsets_to_operating_expenditures'
    ]
].T

comparison.set_index('name.cand')[
    [
     'individual_itemized_contributions',
     'individual_unitemized_contributions',
     'transfers_from_affiliated_committee',
    ]
].plot(kind='barh', stacked=True, figsize=(12,8))

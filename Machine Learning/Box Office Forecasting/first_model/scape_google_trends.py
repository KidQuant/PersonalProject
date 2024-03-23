import pandas as pd
import time
from pytrends.request import TrendReq

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrends = TrendReq()

google1 = pd.read_csv("google_name7.csv")
google1["ID"] = google1["ID"].str.replace("%2F","/")

i=0
while i < len(google1):
    kw_list = list(google1["ID"][i:i + 5])

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list, timeframe='2017-01-01 2018-03-01', geo='US', gprop='')
    interest_over_time_df = pytrend.interest_over_time()
    interest_over_time_df.drop(['isPartial'], axis=1, inplace=True)
    if i != 0:
        maxnum2 = interest_over_time_df[kw_list[0]].max()
        interest_over_time_df.drop([kw_list[0]], axis=1, inplace=True)
        interest_over_time_df = interest_over_time_df / maxnum2 * maxnum
        interest_over_time_df = interest_over_time_df.reset_index()
        interest_over_time_df = pd.merge(interest_over_time_df, interest_over_time_df2,  how='left', left_on=['date'], right_on = ['date'])
    else:
        interest_over_time_df = interest_over_time_df.reset_index()
    maxnum = interest_over_time_df[kw_list[-1]].max()
    interest_over_time_df2 = interest_over_time_df
    i = i + 4
    time.sleep(3)

interest_over_time_df

import pandas as pd
import numpy as np
from datetime import datetime

rfp_receipts = pd.read_csv('RFP_Itemized_schedule_a.csv')
trump_receipts = pd.read_csv('scheduleatrump.csv')
trump_receipts
rfp_receipts.head()


datetime.strftime(pd.to_datetime(str(test)), '%Y-%m-%d')
rfp_receipts

rfp_receipts['Contribution_Date'] = rfp_receipts['Contribution_Date'].apply(lambda x: datetime.strftime(pd.to_datetime(str(x)), '%Y-%m-%d'))

rfp_receipts['Zip_Code'] = rfp_receipts['Zip_Code'].apply(lambda x: int(str(x)[:5]))

cleaned = rfp_receipts.drop_duplicates(subset=['Last_Name', 'Zip_Code', 'Amount'], keep='last')
cleaned[cleaned['Last_Name'] == 'CASSIDY']


trump_receipts['Aggrergate'].mean()

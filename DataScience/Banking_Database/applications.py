import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import email, getpass, imaplib, os, re
from datetime import datetime

detach_dir = '.'
user = input('Enter your Gmail username:')
pwd = getpass.getpass('Enter your password:')

m = imaplib.IMAP4_SSL('imap.gmail.com')
m.login(user, pwd)

m.select('"Job Applications"')

resp, items = m.search(None, 'All')
items = items[0].split()

text = []
dates = []
subjects = []

for emailid in items:

    resp, data = m.fetch(emailid, '(RFC822)')

    email_body = data[0][1]

    mail = email.message_from_bytes(email_body)

    subjects.append(email.header.decode_header(mail['Subject'])[0][0])

    date_tuple = email.utils.parsedate_tz(mail['Date'])
    dates.append(datetime.fromtimestamp(email.utils.mktime_tz(date_tuple)))

    if mail.is_multipart():
        text.append(mail.get_payload(0).get_payload())
    else:
        text.append(mail.get_payload())

df = pd.DataFrame(data={'Date':dates, 'Subject':subjects, 'Text':text})
df.head()
df.tail()

df['Time'] = df['Date'].apply(lambda x: x.time())
df['Day'] = df['Date'].apply(lambda x: x.weekday()).map({0:'Mon', 1:'Tues', 2:'Weds', 3:'Thur', 4:'Fri', 5:'Sat', 6:'Sun'})
df['Hour'] = df['Time'].apply(lambda x: x.hour)
df = df[['Date', 'Time', 'Day', 'Hour', 'Subject', 'Text']]

df.head()
df.tail()
df.info()
df.to_csv('andres_job_applications.csv', index = False)

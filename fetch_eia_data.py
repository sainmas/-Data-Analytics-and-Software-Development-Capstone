"""
This script will send a request to the EIA API for current energy information with the provided parameters.
"""

from datetime import datetime
from datetime import timedelta
import requests
import pandas as pd
import auth

# determine date to use
now = datetime.today()

# create a time delta object to find two days ago
delta = timedelta(days=2)

# use datetime arithmetic to get two days ago.
two_days_ago = now - delta

# convert datetime to valid format for the API call
def change_to_api_format(dt: datetime) -> str:
  return dt.strftime("%Y-%m-%dT%H")

now_str = change_to_api_format(now)
then_str = change_to_api_format(two_days_ago)

"""
API route used:
"Electricity",
"Electric Power Operations (Daily And Hourly)"
"Hourly Demand, Demand Forecast, Generation, and Interchange"

Link for easy access to website: https://www.eia.gov/opendata/browser/electricity/rto/region-data

Current parameters set within 'params' variable below (which can be modified for filtering directly from api)

frequency: 
hourly

facets[respondent]:
NW - Pacific Northwest,
SCL - Seattle City Light

facets[type]:
D - Demand,
DF - Day-ahead demand forecast,
NG - Net Generation

start & end
2023-04-21T00" - "2023-04-22T00"
"""

params = {
    "frequency": "hourly",
    "data[0]": "value",
    "facets[respondent][]": ["NW", "SCL"],
    "facets[type][]": ["D", "DF", "NG"],
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "start": then_str,
    "end": now_str,
    "offset": 0,
    "length": 5000
}

print("Fetching data")

# api query link
URL = auth.URL

# save request in response variable
response = requests.get(URL, params=params)

# convert response into json
json_data = response.json()['response']['data']

print("Transforming data")

# flattening the dataset
# Convert the nested JSON object to a flat DataFrame
df = pd.json_normalize(json_data, meta=['period', 'respondent', 'type'])

# Rename columns for clarity
df.columns = ['date', 'respondent', 'respondent_full', 'type', 'type_full', 'value', 'unit']

# convert date string to datetime object, match the formatting.
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%dT%H")

print(df)
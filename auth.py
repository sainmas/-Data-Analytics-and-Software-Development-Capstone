"""
This script will authenticate with the Google Cloud Server using the credentials in the .env file (KEY_PATH).
For more information on how to set up your key json and key path, check: https://cloud.google.com/bigquery/docs/authentication/service-account-file
"""

from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv.main import load_dotenv
import os

# load .env variables
load_dotenv()

# Set the key path to the authentication file path
key_path = os.getenv('KEY_PATH')

# Create the authentication credentials
credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

# Create a Client() object and use your credentials to authenticate and list the project
client = bigquery.Client(credentials=credentials,
                         project=credentials.project_id)

# note for team: replace xxxxxx with your API Key
API_KEY = os.getenv('API_KEY')

# EIA API URL
URL = "https://api.eia.gov/v2/electricity/rto/region-data/data/?api_key=" + API_KEY

# Set your projectID and initialize the BigQuery client
PROJECT_ID = os.getenv('PROJECT_ID')

# Set up dataset and table setup in the BigQuery database, then replace these names with yours
DATASET_ID = os.getenv('DATASET_ID')
TABLE_ID = os.getenv('TABLE_ID')

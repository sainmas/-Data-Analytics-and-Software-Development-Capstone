# Data Analytics and Software Development Capstone Project

Capstone project for the Data Analytics and Software Development, Associate of Applied Sciences degree from Green River College. This application runs a script every 24 hours that will pull relevant energy data from the Energy Information Administration (EIA) API, process and clean it, then will send it to a BigQuery database for storage.

## Authors 
Mason Sain, Addison Farley, RJ Trenchard, Will Castillo, Noah Lanctot

## Running the Program

To run this application, you will need to have a Google Cloud account with BigQuery enabled. From Google Cloud, you need to create and download an account service key json (https://console.cloud.google.com/iam-admin/serviceaccounts/) and add that file to your program's root directory.

Adjust the values in the 'constants.env' file as applicable.

KEY_PATH is found in the first link in the helpful links section. 
PROJECT_ID is what you named your project in the BigQuery client.
DATASET_ID is what you named your database in the BigQuery client.
TABLE_ID is what you named your table in the BigQuery client.
API_KEY is the API key you created for yourself on the eia website. Fourth link in the links section. 

Once the 'constants.env' file is updated, the program can be ran through main.py via a local machine or a hosted machine 24/7. This updates every 24 hours and will pull 2 days worth of energy data from the EIA API.

## Helpful links
Google Clound Key Creation: 
https://cloud.google.com/iam/docs/keys-create-delete#creating 
Google Cloud BigQuery Project Manager: https://console.cloud.google.com/iam-admin/serviceaccounts/
Google Cloud Authentication: https://cloud.google.com/bigquery/docs/authentication/service-account-file
EIA API Registration: https://www.eia.gov/opendata/

Make sure to secure the JSON file and avoid sharing it publicly. It contains sensitive information that grants access to your Google Cloud resources. 

![System Diagram](https://github.com/AddisonFarley/SDEV-280-Capstone/assets/93640684/be911ae9-fa23-4860-b27a-48c698645905)

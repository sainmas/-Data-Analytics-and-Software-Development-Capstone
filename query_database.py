"""
This script will take the information received from the EIA API, process for DB consumption, then update the
BigQuery database.
"""

import time
import auth
import fetch_eia_data as fetch

# import .env variables
PROJECT_ID = auth.PROJECT_ID
DATASET_ID = auth.DATASET_ID
TABLE_ID = auth.TABLE_ID
CLIENT = auth.client

print("Updating BigQuery Database")

# start of the sql statement
sql = f"INSERT INTO `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}` VALUES "

# loop over whole dataframe & adds line to insert statement
df = fetch.df

for row in df.itertuples():
    # adding onto the sql statement given to BigQuery
    sql = (sql +
           f"('{row.date}','{row.respondent}','{row.respondent_full}','{row.type}','{row.type_full}',{row.value},'{row.unit}'),")

# removing final , and adding a ;
sql = (sql[:-1] + ";")
# send over the insert statement to BigQuery
insert_job = CLIENT.query(sql)

print("Checking for duplicates")

# code waits 3 seconds for the database to fully update before replacing rows
time.sleep(3)

# creates and replaces our current table with one with no duplicates (could take a while if a ton of rows)
sql = (f"""
create or replace table `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`  as (
  select * except(row_num) from (
      select *,
        row_number() over ( partition by `date`, `respondent`,`respondent_full`,`type`,`type_full`,`value`,`unit` order by `date`, `respondent`,`respondent_full`,`type`,`type_full`,`value`,`unit` ) row_num
      from
      `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}` ) t
  where row_num=1
)
""")

# send dupe check to BigQuery
insert_job = CLIENT.query(sql)

print("Finished")

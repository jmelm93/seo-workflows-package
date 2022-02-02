
from google.oauth2 import service_account
from google.cloud import bigquery

import pandas as pd

from datetime import datetime

import os

import logging

# US os.path.join to get the path of current file
# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'service_account.json')


def dict_to_bigquery(service_account_json, input_dict):

    table_id = input_dict["table_id"]
    
    # Add 2 items to dict object
    input_dict["date"] = datetime.today().strftime('%Y-%m-%d')
    input_dict["hour"] = datetime.today().strftime('%H:%M')
    
    # Need to do this to ensure all necessary schema fields are included
    # makes it so we don't have to use unnecessary fields in each individual script
    load_dict = []
    load_dict.append(
        dict(
            tool=input_dict.get("tool", "None"),
            date=input_dict.get("date", "None"),
            hour=input_dict.get("hour", "None"),
            uid=input_dict.get("uid", "None"),
            report_name=input_dict.get("report_name", "None"),
            file_name=input_dict.get("file_name", "None"),
            file_size=input_dict.get("file_size", "None"),
            run_time_full_script=input_dict.get("run_time_full_script", "None"),
            run_time_ExcelWriter=input_dict.get("run_time_ExcelWriter", "None"),
            run_time_ngrams=input_dict.get("run_time_ngrams", "None"),
            run_time_NgamsAndQql=input_dict.get("run_time_NgamsAndQql", "None"),
            job_status=input_dict.get("job_status", "None"),
            error_message=input_dict.get("error_message", "None"),
            domains_1=input_dict.get("domains_1", "None"),
            domains_2=input_dict.get("domains_2", "None"),
            )
        )

    credentials = service_account.Credentials.from_service_account_file(service_account_json)
    
    scoped_credentials = credentials.with_scopes(scopes=[
        'https://www.googleapis.com/auth/cloud-platform'
    ])

    client = bigquery.Client(credentials=scoped_credentials) # was issing this

    # have to pass an index since the dict is using scalar values
    # scalar = simple single numeric value
    load_dict_df = pd.DataFrame(load_dict, index=[0])    

    logging.debug(load_dict)
    
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_APPEND")

    job = client.load_table_from_dataframe(load_dict_df, table_id, job_config=job_config)  # Make an API request.
    
    job.result()  # Wait for the job to complete.
    
    table = client.get_table(table_id)  # Make an API request.
    
    print(
        "Loaded {} rows and {} columns to {}".format(
            table.num_rows, len(table.schema), table_id
        )
    )

    return logging.debug(f"Finished writing the 'write_to_bigquery' method")
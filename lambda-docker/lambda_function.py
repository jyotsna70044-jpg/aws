import json
import boto3
# import pandas as pd
# import awswrangler as wr

s3 = boto3.client('s3')


def lambda_handler(event, context):
    # TODO implement
    print("event=", event)
    record = event.get('Records')
    print(record)
    for e in record:
        s3_event_type = e.get('eventName')
        print(s3_event_type)
        s3_bucket = e['s3']['bucket']['name']
        key = e['s3']['object']['key']
        print(f"{s3_event_type},{s3_bucket},{key}")
        read_from_s3(s3_event_type, s3_bucket, key)
    return {
        'statusCode': 201,
        'body': json.dumps('Hello from Lambda!')
    }


def read_from_s3(s3_event_type, bucket_name, input_file_key):
    try:
        df = ''
        s3_input_path = f"s3://{bucket_name}/{input_file_key}"
        # Read based on file type
        if input_file_key.endswith(".csv"):
            df = wr.s3.read_csv(s3_input_path)
        elif input_file_key.endswith(".json"):
            df = wr.s3.read_json(s3_input_path)
        elif input_file_key.endswith(".parquet"):
            df = wr.s3.read_parquet(s3_input_path)
        else:
            print("Unsupported file format for reading.")
            # Handle other formats or raise an error
        print(df.head())
        write_to_s3(df,bucket_name)


    except Exception as e:
        print(f"Error reading file from S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error reading file: {str(e)}")
        }


def write_to_s3(df,bucket_name):
    output_key = "silver/emp.parquet"
    s3_output_path = f"s3://{bucket_name}/{output_key}"
    try:
        wr.s3.to_parquet(df=df, path=s3_output_path, index=False)  # index=False to avoid writing pandas index
    except Exception as e:
        print(f"Error reading file from S3: {e}")

import json
import boto3
import csv
import io

s3_client = boto3.client('s3')


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


def read_from_s3(s3_event_type, s3_bucket, object_key):
    # Get the object from S3
    response = s3_client.get_object(Bucket=s3_bucket, Key=object_key)
    csv_content = response['Body'].read().decode('utf-8')

    # Read the CSV data
    csv_file = io.StringIO(csv_content)
    reader = csv.reader(csv_file)

    # Skip header if present
    header = next(reader, None)
    if header:
        print(f"CSV Header: {header}")

    # Process each row
    for row in reader:
        print(f"Processing row: {row}")
        # Add your data processing logic here

    return {
        'statusCode': 200,
        'body': f'Successfully processed {object_key} from {s3_bucket}'
    }

import boto3
import json
import time

# Replace with your SQS queue URL
QUEUE_URL = 'https://sqs.ap-south-1.amazonaws.com/412040338345/first-queue'


def process_message(message_body):
    """Simulates processing of an SQS message."""
    print(f"Processing message: {message_body}")
    # Add your actual message processing logic here
    time.sleep(1)  # Simulate work


def receive_and_process_sqs_messages():
    """Receives and processes messages from an SQS queue."""
    sqs_client = boto3.client('sqs')
    while True:
        try:
            response = sqs_client.receive_message(
                QueueUrl=QUEUE_URL,
                MaxNumberOfMessages=1,  # Receive up to 1 message at a time
                WaitTimeSeconds=10  # Use long polling for up to 10 seconds
            )

            if 'Messages' in response:
                for message in response['Messages']:
                    message_body = json.loads(message['Body'])
                    process_message(message_body)

                    # Delete the message after successful processing
                    sqs_client.delete_message(
                        QueueUrl=QUEUE_URL,
                        ReceiptHandle=message['ReceiptHandle']
                    )
                    print(f"Message deleted: {message['MessageId']}")
            else:
                print("No messages in queue. Waiting...")
            time.sleep(5)  # Wait before polling again if no messages were found
        except Exception as e:
            print(f"Error receiving or processing messages: {e}")
            time.sleep(10)  # Wait longer on error


if __name__ == "__main__":
    receive_and_process_sqs_messages()

import boto3
import json

# Replace with your SQS queue URL
QUEUE_URL = 'https://sqs.ap-south-1.amazonaws.com/412040338345/first-queue'


def send_sqs_message(message_body):
    """Sends a message to an SQS queue."""
    sqs_client = boto3.client('sqs')
    try:
        response = sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=json.dumps(message_body)  # SQS messages are strings, so serialize JSON
        )
        print(f"Message sent successfully. Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"Error sending message: {e}")


if __name__ == "__main__":
    sample_message = {"data": "This is a test message", "timestamp": "2025-11-09T03:00:00Z"}
    send_sqs_message(sample_message)

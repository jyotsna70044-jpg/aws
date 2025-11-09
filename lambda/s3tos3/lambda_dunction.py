import json

def lambda_handler(event, context):
    """
    This function demonstrates a simple "Hello World" AWS Lambda function.
    It takes an event, and optionally a 'name' from the event,
    and returns a greeting message.
    """
    
    # Extracting information from the event
    # For example, if the event is {"name": "World"}
    name = event.get('name', 'World') 
    
    # Constructing the response
    response_message = f"Hello, {name}!"
    
    # Logging to CloudWatch (optional but good practice)
    print(f"Lambda invoked with name: {name}")
    
    # Returning a structured response, often in JSON format
    return {
        'statusCode': 200,
        'body': json.dumps(response_message)
    }
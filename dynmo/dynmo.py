import boto3
# Create a DynamoDB resource object
dynamodb = boto3.resource('dynamodb')
# Specify your DynamoDB table name
table_name = 'emp' # Replace with your actual table name

def put_item(emp):
    table = dynamodb.Table(table_name)
    item_data = {
        'id': row[0],  # Replace with your primary key and value
        'emp_name': row[1],
        'dept_id': row[2],
        'salary': row[3],
        'hire_date': row[4]
    }

    try:
        response = table.put_item(Item=item_data)
        print("Item added successfully:")
        print(response)
    except Exception as e:
        print(f"Error adding item: {e}")
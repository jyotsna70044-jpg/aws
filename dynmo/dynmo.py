import boto3
# Create a DynamoDB resource object
dynamodb = boto3.resource('dynamodb')
# Specify your DynamoDB table name
table_name = 'emp' # Replace with your actual table name

def put_item(emp):
    table = dynamodb.Table(table_name)
    # Define the item to be added as a dictionary
    # Ensure your primary key attributes are included
    item_data = {
        'id': emp['EmployeeID'],  # Replace with your primary key and value
        'emp_name': emp['Name'],
        'dept_id': emp['DepartmentID'],
        'hire_date': emp['HireDate'],
        'salary': emp['Salary'],
    }

    try:
        response = table.put_item(Item=item_data)
        print("Item added successfully:")
        print(response)
    except Exception as e:
        print(f"Error adding item: {e}")
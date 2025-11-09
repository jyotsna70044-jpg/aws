import boto3

# Create a DynamoDB resource object
dynamodb = boto3.resource('dynamodb')
# Specify your DynamoDB table name
table_name = 'emp'  # Replace with your actual table name


def put_item(emp):
    table = dynamodb.Table(table_name)
    item_data = {
        'id': emp['id'],  # Replace with your primary key and value
        'emp_name': emp['emp_name'],
        'dept_id': emp['dept_id'],
        'hire_date': emp['hire_date'],
        'salary': emp['salary'],
    }

    try:
        response = table.put_item(Item=item_data)
        print("Item added successfully:")
        print(response)
    except Exception as e:
        print(f"Error adding item: {e}")


import boto3


# def get_item(pk, sk=None):
#     table = dynamodb.Table(table_name)
#     # Retrieve an item
#     response = table.get_item(
#         Key={
#             'id': pk  # Replace with your attribute and value
#         }
#     )
#     item = response.get('Item')
#     if item:
#         print("Item retrieved:", item)
#     else:
#         print("Item not found.")
#
# get_item(1)
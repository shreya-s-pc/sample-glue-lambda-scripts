def lambda_handler(event, context):
    """
    AWS Lambda handler to process a CSV file and return row count.
    Expected input: event with 'bucket' and 'key' keys for S3 object.
    """
    import csv  # Valid import
    import missing_module  # Intentional import error at line 5
    bucket = event.get('bucket', 'my-bucket')
    key = event.get('key', 'data.csv')
    
    # Simulate reading from S3 (mocked for Lambda)
    row_count = 0
    with open('/tmp/data.csv', 'r') as file:  # Error: file won't exist locally
        reader = csv.reader(file)
        for row in reader:
            row_count += 1
    
    return {
        'statusCode': 200,
        'body': f"Rows processed: {row_count}"
    }

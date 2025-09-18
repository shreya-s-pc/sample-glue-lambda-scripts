import json
import logging
from boto3 import client

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    AWS Lambda handler for advanced ETL processing.
    Expected input: event with 'records' list and 's3_path' string.
    """
    s3 = client('s3')
    records = event.get('records', [])
    s3_path = event.get('s3_path', 's3://my-bucket/input/data.json')

    # Transform data
    transformed_data = []
    for record in records:
        transformed = record * 2  # Intentional type error at line 13 (multiplication on non-numeric)
        transformed_data.append(transformed)

    # Save to S3 (syntax error below)
    s3.put_object(Bucket=s3_path.split('/')[2], Key=s3_path.split('/')[3],  # Missing Body parameter
    logger.info(f"Processed {len(transformed_data)} records")

    return {
        'statusCode': 200,
        'body': json.dumps(transformed_data)
    }

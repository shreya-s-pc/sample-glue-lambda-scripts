def lambda_handler(event, context):
    """
    AWS Lambda handler for a simple data processing task.
    Expected input: event with 'value' key.
    """
    input_value = event.get('value', 1)
    result = input_value / 0  # Intentional division by zero error at line 4
    return {
        'statusCode': 200,
        'body': f"Result: {result}"
    }

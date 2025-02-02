import json
import boto3


def lambda_handler(event, context):
    # Extract customer input from the Connect event
    customer_choice = event['Details']['Parameters'].get('customerInput')
    
    # Define dynamic routing logic with queue names containing spaces
    routing = {
        "1": "Event Queue",  # Event Photography with space
        "2": "Commercial Content Queue", # Commercial Content with space
        "3": "Music Video Queue",        # Music Video with space
        "4": "Corporate Video Queue",    # Corporate Video with space
        "5": "General Inquiry Queue"     # General Inquiry with space
    }
    
    # Default queue if no valid input
    default_queue = "General Inquiry Queue"
    
    # Select queue based on customer input
    selected_queue = routing.get(customer_choice, default_queue)
    
    # Prepare response for Amazon Connect
    response = {
        "QueueName": selected_queue,
        "Message": f"Routing to {selected_queue}."
    }
    
    # Log the response
    print(f"Routing decision: {response}")
    
    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

    


import json
import requests
import os
import logging 


def lambda_handler(event, context):
    # Parse data from HR webhook
    body = json.loads(event['body'])
    user_email = body.get('email')

    
    # App API details
    api_token = os.environ['APP_API_KEY']
    api_url = f"https://api.customapp.com/users?email={user_email}"
    
    # Lookup user
    response = requests.get(api_url, headers={"Authorization": f"Bearer {api_token}"})
    user_data = response.json()
    
    if response.status_code == 200 and user_data:
        user_id = user_data[0]['id']
        # Deactivate user
        deactivate_url = f"https://api.customapp.com/users/{user_id}/deactivate"
        result = requests.post(deactivate_url, headers={"Authorization": f"Bearer {api_token}"})
        
        
        if result.status_code in [200, 204]:
            return {"statusCode": 200, "body": json.dumps({"message": "User deactivated."})}
        else:
            return {"statusCode": 500, "body": json.dumps({"error": "Deactivation failed."})}
    
    return {"statusCode": 404, "body": json.dumps({"error": "User not found."})}
    

##import logging
##logger = logging.getLogger()
##logger.setLevel(logging.INFO)

##def lambda_handler(event, context):
    ...
 ##   result = {"status": "User deactivated", "user_id": user_id}
##  logger.info(json.dumps(result))  # This goes into CloudWatch
##    return result




import requests

OKTA_DOMAIN = "https://dev-123456.okta.com"
API_TOKEN = "your_okta_api_token_here"

HEADERS = {
    "Authorization": f"SSWS {API_TOKEN}",
    "Content-Type": "application/json"
}

def create_user(first_name, last_name, email, group_id=None):
    url = f"{OKTA_DOMAIN}/api/v1/users?activate=true"
    payload = {
        "profile": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "login": email
        },
        "credentials": {
            "password": { "value": "TempPassword123!" }
        }
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    
    if response.status_code == 200:
        user_id = response.json()["id"]
        print(f"✅ User {email} created successfully.")
        if group_id:
            assign_user_to_group(user_id, group_id)
    else:
        print(f"❌ Error creating user: {response.status_code} - {response.text}")

def assign_user_to_group(user_id, group_id):
    url = f"{OKTA_DOMAIN}/api/v1/groups/{group_id}/users/{user_id}"
    response = requests.put(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"✅ User added to group {group_id}")
    else:
        print(f"❌ Failed to add user to group: {response.status_code} - {response.text}")

# Example usage
if __name__ == "__main__":
    create_user(
        first_name="Alice",
        last_name="Smith",
        email="alice.smith@example.com",
        group_id="00g12345678EXAMPLE"  # Optional: remove if not assigning to group
    )
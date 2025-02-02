"""
This is the basic tests for the PUT method API Calls for the sample APIs , where we are just validating
the status code of the response in a positive scenario.
"""
import requests
import json

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the ENDPOINT and PAYLOAD
ENDPOINT = '/posts/1'  # Updating post with ID 1
PAYLOAD = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}


# Function to send a PUT request
def send_put_request(ENDPOINT, PAYLOAD):
    url = f"{BASE_URL}{ENDPOINT}"

    print(f"Sending PUT request to: {url}")
    print(f"PAYLOAD: {json.dumps(PAYLOAD, indent=4)}")

    # Send PUT request
    response = requests.put(url, json=PAYLOAD)
    response_data = response.json()  # Get the response data as a dictionary
    user_id = response_data.get('id')  # Access the 'id' key
    print(f"User ID: {user_id}")

    # Check if the request was successful (200 OK)
    if response.status_code == 200:
        print("Request successful!")
        print("Response Status Code:", response.status_code)
        print("Response Data:", json.dumps(response.json(), indent=4))
    else:
        print(f"Failed! Status Code: {response.status_code}")
        print("Response Data:", json.dumps(response.json(), indent=4))

# Call the function to send PUT request
send_put_request(ENDPOINT, PAYLOAD)

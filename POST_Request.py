"""
This is the basic tests for the POST method API Calls for the sample APIs , where we are just validating
the status code of the response in a positive scenario.
"""
import requests
import json

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the endpoint and payload
ENDPOINT = '/posts'
PAYLOAD = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

def send_post_request(ENDPOINT, PAYLOAD):
    url = f"{BASE_URL}{ENDPOINT}"

    print(f"Sending POST request to: {url}")
    print(f"Payload: {json.dumps(PAYLOAD, indent=4)}")

    # Send POST request
    response = requests.post(url, json=PAYLOAD)

    # Check if the request was successful (201 Created)
    if response.status_code == 201:
        print("Request successful!")
        print("Response Status Code:", response.status_code)
        print("Response Data:", json.dumps(response.json(), indent=4))
    else:
        print(f"Failed! Status Code: {response.status_code}")
        print("Response Data:", json.dumps(response.json(), indent=4))


# Call the function to send POST request
send_post_request(ENDPOINT, PAYLOAD)


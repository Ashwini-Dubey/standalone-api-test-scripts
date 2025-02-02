"""
This is the basic tests for the GET method API Calls for the sample APIs , where we are just validating
the status code of the response in a positive scenario.
"""
import requests
import json

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the endpoint
ENDPOINT = '/users'

def send_get_request(BASE_URL,ENDPOINT):
    url = f"{BASE_URL}{ENDPOINT}"

    try:
        # Send GET request
        response = requests.get(url)
        print("####Printing the Response Encoding####")
        print(response.encoding)
        print("####Printing the Response in Text Format####")
        print(response.text)
        print("####Printing the Response in JSON Format####")
        print(response.json)
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()  # Parse JSON response
            print(json.dumps(data, indent=4))  # Pretty print the JSON data
        else:
            print("Failed to fetch data, status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred:",e)

# Call the function to send GET request
send_get_request(BASE_URL,ENDPOINT)



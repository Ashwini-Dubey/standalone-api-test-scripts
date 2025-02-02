"""
This is the basic tests for the DELETE method API Calls for the sample APIs , where we are just validating
the status code of the response in a positive scenario.
"""

import requests

# Base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Define the endpoint
ENDPOINT = '/posts/1'  # Deleting post with ID 1


# Function to send a DELETE request
def send_delete_request(ENDPOINT):
    url = f"{BASE_URL}{ENDPOINT}"

    print(f"Sending DELETE request to: {url}")

    # Send DELETE request
    response = requests.delete(url)

    # Check if the request was successful (usually 200 or 204 for DELETE)
    if response.status_code in [200, 204]:
        print(f"Delete request successful! Status Code: {response.status_code}")
    else:
        print(f"Failed to delete! Status Code: {response.status_code}")

# Call the function to send DELETE request
send_delete_request(ENDPOINT)

import os
import json
import urllib.request
from urllib.error import HTTPError
import base64

# Get the directory path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the test cases directory
test_cases_directory = os.path.join(script_dir, 'CodeBeamer', 'test_results', 'test_cases')

# Directory where test case JSON files are stored
#test_cases_directory = "Codebeamer/test_results/test_cases"

# URL of the server endpoint to add test cases
url = "http://20.198.16.233:8080/cb/rest/item"

# Credentials for Basic Authentication
username = "poorvashayadav"
password = "poorvasha.yadav"

# Function to read JSON data from a file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Main function to add test cases
def add_test_cases():
    # Encode credentials for Basic Authentication
    auth_string = f"{username}:{password}"
    auth_bytes = auth_string.encode('utf-8')
    base64_bytes = base64.b64encode(auth_bytes)
    base64_auth_string = base64_bytes.decode('utf-8')

    # Iterate over each JSON file in the directory
    for filename in os.listdir(test_cases_directory):
        if filename.endswith('.json'):
            file_path = os.path.join(test_cases_directory, filename)
            test_case = read_json(file_path)
            
            # Prepare request data
            data = json.dumps(test_case).encode('utf-8')
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Basic {base64_auth_string}'
            }
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            
            try:
                with urllib.request.urlopen(req) as response:
                    print(f"Successfully added test case: {test_case['name']}")
            except HTTPError as e:
                print(f"Failed to add test case: {test_case['name']}, Status Code: {e.code}, Response: {e.read().decode('utf-8')}")

if __name__ == "__main__":
    add_test_cases()

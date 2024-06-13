import os
import json
import urllib.request
from urllib.error import HTTPError

# Directory where test case JSON files are stored
test_cases_directory = "Codebeamer/testresults/test_cases"

# URL of the server endpoint to add test cases
url = "http://20.198.16.233:8080/cb/rest/item"

# Function to read JSON data from a file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Main function to add test cases
def add_test_cases():
    # Iterate over each JSON file in the directory
    for filename in os.listdir(test_cases_directory):
        if filename.endswith('.json'):
            file_path = os.path.join(test_cases_directory, filename)
            test_case = read_json(file_path)
            
            # Prepare request data
            data = json.dumps(test_case).encode('utf-8')
            headers = {'Content-Type': 'application/json'}
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            
            try:
                with urllib.request.urlopen(req) as response:
                    print(f"Successfully added test case: {test_case['name']}")
            except HTTPError as e:
                print(f"Failed to add test case: {test_case['name']}, Status Code: {e.code}, Response: {e.read().decode('utf-8')}")

if __name__ == "__main__":
    add_test_cases()

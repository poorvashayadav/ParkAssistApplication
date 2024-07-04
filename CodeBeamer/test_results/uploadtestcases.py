import os
import json
import urllib.request
from urllib.error import HTTPError, URLError
import base64
import platform

# Determine the correct path based on the operating system and environment
if platform.system() == 'Windows':
    test_cases_directory = "CodeBeamer\\test_results\\test_cases"
else:
    # Get the directory path of the current script for non-Windows environments
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_cases_directory = os.path.join(script_dir, 'test_cases')

# Print paths for debugging
print(f"Operating System: {platform.system()}")
print(f"Test cases directory: {test_cases_directory}")

# URL of the server endpoint to add test cases
url = "http://20.198.16.233:8080/cb/rest/item"
base_url = "http://20.198.16.233:8080/cb/rest"
test_run_url = f"{base_url}/testRun"

# Credentials for Basic Authentication
username = os.getenv('cb_user')
password = os.getenv('cb_password')

# Function to read JSON data from a file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Main function to add test cases
def add_test_cases():
    if not username or not password:
        print("Username or password environment variables not set.")
        return

    # Encode credentials for Basic Authentication
    auth_string = f"{username}:{password}"
    auth_bytes = auth_string.encode('utf-8')
    base64_bytes = base64.b64encode(auth_bytes)
    base64_auth_string = base64_bytes.decode('utf-8')

    # Check if the directory exists
    if not os.path.isdir(test_cases_directory):
        print(f"Directory does not exist: {test_cases_directory}")
        return

    # Get list of files in the directory
    files = [f for f in os.listdir(test_cases_directory) if f.endswith('.json')]
    print(f"Found {len(files)} JSON files in the directory.")

    # Iterate over each JSON file in the directory
    for filename in files:
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
                response_body = response.read().decode('utf-8')
                print(f"Successfully added test case: {test_case.get('name', filename)}")
                print(f"Response: {response_body}")
        except HTTPError as e:
            error_message = e.read().decode('utf-8')
            print(f"Failed to add test case: {test_case.get('name', filename)}, Status Code: {e.code}")
            print(f"Error: {error_message}")
        except URLError as e:
            print(f"Failed to add test case: {test_case.get('name', filename)}")
            print(f"Error: {e.reason}")

# Function to fetch item IDs (test case IDs) from CodeBeamer
def fetch_items():
    auth_string = f"{username}:{password}"
    base64_auth_string = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
    items_api_url = f"{base_url}/project/39/category/108531/items"

    req = urllib.request.Request(items_api_url, headers={'Authorization': f'Basic {base64_auth_string}'})

    try:
        with urllib.request.urlopen(req) as response:
            response_body = response.read().decode('utf-8')
            data = json.loads(response_body)
            item_ids = [item['id'] for item in data.get('items', [])]
            print(f"Fetched item IDs: {item_ids}")
            return item_ids
    except urllib.error.HTTPError as e:
        print(f"Failed to fetch items, Status Code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Failed to fetch items: {e.reason}")

    return []

# Function to create a test run with query parameters
def create_test_run(test_case_ids):
    auth_string = f"{username}:{password}"
    base64_auth_string = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')

    # Prepare headers
    headers = {
        'Authorization': f'Basic {base64_auth_string}',
        'Accept': '*/*', # Accept any content type
        'Accept-Encoding': 'gzip, deflate, br' 
    }

    # Construct the URL with query parameters
    url_with_params = f"{test_run_url}?testCaseIds={','.join(map(str, test_case_ids))}"

    # Create the request
    req = urllib.request.Request(url_with_params, headers=headers, method='POST')

    try:
        # Enable verbose debugging
        urllib.request.urlopen(req).debuglevel = 1

        # Send the request
        with urllib.request.urlopen(req) as response:
            # Check if response is gzip or deflate encoded
            if response.info().get('Content-Encoding') == 'gzip':
                response_body = gzip.GzipFile(fileobj=response).read().decode('utf-8')
            elif response.info().get('Content-Encoding') == 'deflate':
                response_body = io.BytesIO(response.read()).read().decode('utf-8')
            else:
                response_body = response.read().decode('utf-8')

            print(f"Successfully created test run.")
            print(f"Response: {response_body}")
    except urllib.error.HTTPError as e:
        error_message = e.read().decode('utf-8')
        print(f"Failed to create test run, Status Code: {e.code}")
        print(f"Error: {error_message}")
    except urllib.error.URLError as e:
        print(f"Failed to reach the server: {e.reason}")

if __name__ == "__main__":
    item_ids = fetch_items()
    if item_ids:
        create_test_run(item_ids)
    else:
        print("No item IDs fetched.")

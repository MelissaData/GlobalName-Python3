
import json
import requests
import argparse
import urllib.parse

def main():
  base_service_url = "https://globalname.melissadata.net/"
  service_endpoint = "V3/WEB/GlobalName/doGlobalName"; #please see https://www.melissa.com/developer/global-name for more endpoints

  # Create an ArgumentParser object
  parser = argparse.ArgumentParser(description='Global Name command line arguments parser')

  # Define the command line arguments
  parser.add_argument('--license', '-l', type=str, help='License key')
  parser.add_argument('--fullname', type=str, help='Full name')

  # Parse the command line arguments
  args = parser.parse_args()

  # Access the values of the command line arguments
  license = args.license
  full_name = args.fullname

  call_api(base_service_url, service_endpoint, license, full_name)


def get_contents(base_service_url, request_query):
    url = urllib.parse.urljoin(base_service_url, request_query)
    response = requests.get(url)
    obj = json.loads(response.text)
    pretty_response = json.dumps(obj, indent=4)

    print("\n=============================== OUTPUT ===============================\n")

    print("API Call: ")
    for i in range(0, len(url), 70):
        if i + 70 < len(url):
            print(url[i:i+70])
        else:
            print(url[i:len(url)])
    print("\nAPI Response:")
    print(pretty_response)

def call_api(base_service_url, service_endpoint, license, full_name):
    print("\n============== WELCOME TO MELISSA GLOBAL NAME CLOUD API ==============\n")

    should_continue_running = True
    while should_continue_running:
        input_full_name = ""
        if not full_name:
            print("\nFill in each value to see results")
            input_full_name = input("Full Name: ")
        else:
            input_full_name = full_name

        while not input_full_name:
            print("\nFill in each value to see results")
            if not input_full_name:
                input_full_name = input("\nFull Name: ")

        inputs = {
            "format": "json",
            "full": input_full_name
        }

        print("\n=============================== INPUTS ===============================\n")
        print(f"\t   Base Service Url: {base_service_url}")
        print(f"\t  Service End Point: {service_endpoint}")
        print(f"\t          Full Name: {input_full_name}")

       # Create Service Call
        # Set the License String in the Request
        rest_request = f"&id={urllib.parse.quote_plus(license)}"

        # Set the Input Parameters
        for k, v in inputs.items():
            rest_request += f"&{k}={urllib.parse.quote_plus(v)}"

        # Build the final REST String Query
        rest_request = service_endpoint + f"?{rest_request}"

        # Submit to the Web Service.
        success = False
        retry_counter = 0

        while not success and retry_counter < 5:
            try: #retry just in case of network failure
                get_contents(base_service_url, rest_request)
                print()
                success = True
            except Exception as ex:
                retry_counter += 1
                print(ex)
                return

        is_valid = False;

        if full_name is not None and full_name != "":
            is_valid = True
            should_continue_running = False

        while not is_valid:
            test_another_response = input("\nTest another record? (Y/N)")
            if test_another_response != '':
                test_another_response = test_another_response.lower()
                if test_another_response == 'y':
                    is_valid = True
                elif test_another_response == 'n':
                    is_valid = True
                    should_continue_running = False
                else:
                    print("Invalid Response, please respond 'Y' or 'N'")

    print("\n=============== THANK YOU FOR USING MELISSA CLOUD API ===============\n")

main()

#!/usr/bin/python3

import argparse
from datetime import datetime
import json
import requests
import urllib3
urllib3.disable_warnings()

def upload_results(host, api_key, scanner, result_file, engagement_id, lead_id, environment, verify=False):
    API_URL = f"https://{host}/api/v2"
    IMPORT_SCAN_URL = f"{API_URL}/import-scan/"
    AUTH_TOKEN = f"Token {api_key}"

    headers = {'Authorization': AUTH_TOKEN}

    json_data = {
        'minimum_severity': 'Low',
        'scan_date': datetime.now().strftime("%Y-%m-%d"),
        'verified': False,
        'active': False,
        'engagement': engagement_id,
        'lead': lead_id,
        'scan_type': scanner,
        'environment': environment,
    }

    files = {'file': open(result_file, 'rb')}
    
    response = requests.post(
    IMPORT_SCAN_URL,
    headers=headers,
    files=files,
    json=json_data,
    verify=False here
    )


    return response.status_code

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CI/CD integration for DefectDojo')
    parser.add_argument('--host', help="DefectDojo Hostname", required=True)
    parser.add_argument('--api_key', help="API v2 Key", required=True)
    parser.add_argument('--engagement_id', help="Engagement ID", required=True)
    parser.add_argument('--result_file', help="Scanner file", required=True)
    parser.add_argument('--scanner', help="Type of scanner", required=True)
    parser.add_argument('--product_id', help="DefectDojo Product ID", required=True)
    parser.add_argument('--lead_id', help="ID of the user conducting the testing", required=True)
    parser.add_argument('--environment', help="Environment name", required=True)
    parser.add_argument('--build_id', help="Reference to external build id", required=False)

    # Parse out arguments
    args = vars(parser.parse_args())
    host = args["host"]
    api_key = args["api_key"]
    product_id = args["product_id"]
    result_file = args["result_file"]
    scanner = args["scanner"]
    engagement_id = args["engagement_id"]
    lead_id = args["lead_id"]
    environment = args["environment"]
    build_id = args["build_id"]

    # upload_results(self, host, api_key, scanner, result_file, engagement_id, verify=False): # set verify to False if ssl cert is self-signed
    result = upload_results(host, api_key, scanner, result_file, engagement_id, lead_id, environment)
    if result == 201 :
         print("Successfully uploaded the results to Defect Dojo")
    else:
         print("Something went wrong, please debug " + str(result))

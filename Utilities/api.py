import json

import requests


# Post Request for login #
def post_api_without_access_key(context, api_end_point, payload):
    HEADERS = {'Authorization': 'Bearer ', "Content-Type": "application/json"}
    return requests.post(api_end_point, headers=HEADERS, json=payload)


# Post Request With Access key #
def post_api_with_access_key(context, access_key, api_end_point, payload):
    HEADERS = {'Authorization': 'Bearer ' + access_key, "Content-Type": "application/json"}
    PARAMS = {'type': 'Loader'}
    return requests.post(api_end_point, params=PARAMS, headers=HEADERS, json=payload)

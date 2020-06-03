import json
import requests

def fetch_data(**params):
    url = 'https://api.gnavi.co.jp/PhotoSearchAPI/v3/'
    response = requests.get(url, params=params)
    return response.json()


def extract_data(response):
    for key in response['response'].keys():
        if not key.isdigit():
            continue
        d = response['response'][key]['photo']
        if
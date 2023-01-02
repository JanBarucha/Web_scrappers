import requests
import time
import json
import sys




INPUT_ENDPOINT = 'https://www.reddit.com/r/subreddit.json'
OUTPUT_ENDPOINT = 'https://webhook.site/ca1e0340-5135-44e9-a5a4-798d0fad9d2d'

container = dict()


def fetch_data(web_url, web_endpoint):
    response = requests.get(web_url)
    if response.status_code == 429:
        time.sleep(1)
        print("Sleep 1 sec.....")
        response = fetch_data(web_url, web_endpoint)

    data_json = response.json()

    for item in data_json['data']['children']:
        title = item['data']['title']
        url = item['data']['url']
        container[title] = url

    requests.post(web_endpoint, data=container)
    return response


while True:
    fetch_data(INPUT_ENDPOINT, OUTPUT_ENDPOINT)
    time.sleep(30)

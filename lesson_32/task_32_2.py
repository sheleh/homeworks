# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.

import requests
import time
import json


def get_data(base_url, params):
    request = requests.get(base_url, params=params)
    print('Request sent to : ', request.url)
    return request.json()


def sorting_by_date(data: dict):
    res = {}
    for item in data['data']:
        date = time.ctime(item['created_utc'])
        res[item['created_utc']] = {'Date': date, 'Author': item['author'], 'body': item['body'], 'id': item['id']}

    sorted_by_time = sorted(res.items(), key=lambda x: x[0])
    return sorted_by_time


def save_to_file(sorted_data):
    with open('reddit_dump.json', 'w', encoding='utf-8') as fo:
        json.dump(sorted_data, fo, sort_keys=True, indent=4, separators=(',', ': '))
        print('successfully saved')


if __name__ == '__main__':
    base_url = "https://api.pushshift.io/reddit/comment/search/"
    data = get_data(base_url, {'subreddit': 'python'})
    sorted_data = sorting_by_date(data)
    save_to_file(sorted_data)
# Requests using multiprocessing
# Download all comments from a subreddit of your choice using URL:
# https://api.pushshift.io/reddit/comment/search/ .
# As a result, store all comments in chronological order in JSON and dump it to a file.
# For this task use Threads for making requests to reddit API.

from threading import Thread
import requests
import time
import json


class Thread_req(Thread):
    def __init__(self, url, params):
        super().__init__()
        self.url = url
        self.params = params

    @classmethod
    def sorting_by_date(cls, data):
        res = {}
        for item in data['data']:
            date = time.ctime(item['created_utc'])
            res[item['created_utc']] = {'Date': date, 'Author': item['author'], 'body': item['body'], 'id': item['id']}

        sorted_by_time = sorted(res.items(), key=lambda x: x[0])
        return sorted_by_time

    def save_to_file(self, sorted_data):
        with open(f'{self.params["subreddit"]}.json', 'w', encoding='utf-8') as fo:
            json.dump(sorted_data, fo, sort_keys=True, indent=4, separators=(',', ': '))
            print('successfully saved')

    def run(self):
        request = requests.get(self.url, params=self.params)
        print('Request sent to : ', request.url)
        res = Thread_req.sorting_by_date(request.json())
        self.save_to_file(res)


list_of_keywords = ['xiaomi', 'apple', 'python', 'china']
base_url = "https://api.pushshift.io/reddit/comment/search/"
for k in list_of_keywords:
    thr = Thread_req(base_url, {'subreddit': k})
    thr.start()
    thr.join()
    print(thr)


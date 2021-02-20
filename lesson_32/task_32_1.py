# Download and save to file robots.txt from wikipedia, twitter websites etc.
import requests


def get_robot(url):
    req = requests.get(url + '/robots.txt')
    if req.status_code == 200:
        url = url.split('//')
        with open(f'{url[1]}.txt', 'wb') as f:
            f.write(req.content)


get_robot('https://github.com')
get_robot('https://wikipedia.com')
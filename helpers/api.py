import requests

from config import DATABASE_URL


class RequestHelper:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json'
        }

    def getData(self, url):
        return requests.get(
            url=DATABASE_URL + url,
            headers=self.headers
        ).json()

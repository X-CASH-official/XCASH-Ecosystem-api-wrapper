import imp
import json

import requests


class Helpers():
    def __init__(self):
        pass

    @staticmethod
    def check_url(delegate_url):
        if not delegate_url[-1] == "/":
            return f'{delegate_url}/'
        else:
            return delegate_url

    def process_response(self, response):
        try:
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(err)

    def get_response(self, url):
        print(url)
        response = requests.get(url=url, headers={'Accept': 'application/json',
                                                  "Content-Type": "application/json"})

        return response

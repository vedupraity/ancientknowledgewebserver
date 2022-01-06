import requests
import requests_cache

from config import DATABASE_URL, GITHUB_DATABASE_BRANCH, ENABLE_API_CACHE
from helpers.generic import yaml_to_json


if ENABLE_API_CACHE == 'true':
    requests_cache.install_cache('api_cache')


def fetch_gitub_database_tree():
    git_tree_url = f'https://api.github.com/repos/vedupraity/ancientknowledgedatabase/git/trees/{GITHUB_DATABASE_BRANCH}?recursive=1'
    return requests.get(
        url=git_tree_url,
        headers={
            'Content-Type': 'application/json'
        }
    ).json()


def get_json(url):
    return requests.get(
        url=DATABASE_URL + url,
        headers={
            'Content-Type': 'application/json'
        }
    ).json()


def get_yaml(url):
    response = requests.get(
        url=DATABASE_URL + url,
    )
    response.encoding = 'utf-8'
    
    return yaml_to_json(response.text)


def get_markdown(url):
    response = requests.get(
        url=DATABASE_URL + url,
    )
    response.encoding = 'utf-8'

    return response.text

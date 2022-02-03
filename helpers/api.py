import requests
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache

from config import DATABASE_URL, GITHUB_DATABASE_BRANCH, ENABLE_API_CACHE
from helpers.generic import yaml_to_json


if ENABLE_API_CACHE == 'true':
    request_session = CacheControl(
        requests.Session(),
        cache=FileCache(
            '.api_cache',
            forever=True,
        ),
    )
else:
    request_session = requests.Session()


def fetch_gitub_database_tree():
    git_tree_url = f'https://api.github.com/repos/vedupraity/ancientknowledgedatabase/git/trees/{GITHUB_DATABASE_BRANCH}?recursive=1'
    return request_session.get(
        url=git_tree_url,
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    ).json()


def get_json(url):
    return request_session.get(
        url=DATABASE_URL + url,
        headers={
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    ).json()


def get_yaml(url):
    response = request_session.get(
        url=DATABASE_URL + url,
        headers={
            'Accept': 'text/plain',
            'Content-Type': 'text/plain'
        }
    )
    response.encoding = 'utf-8'
    
    return yaml_to_json(response.text)


def get_markdown(url):
    response = request_session.get(
        url=DATABASE_URL + url,
        headers={
            'Accept': 'text/plain',
            'Content-Type': 'text/plain'
        }
    )
    response.encoding = 'utf-8'

    return response.text

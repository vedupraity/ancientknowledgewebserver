import requests

from config import DATABASE_URL, GITHUB_DATABASE_BRANCH
from helpers.generic import yaml_to_json


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
    return yaml_to_json(requests.get(
        url=DATABASE_URL + url,
    ).text)


def get_markdown(url):
    return requests.get(
        url=DATABASE_URL + url,
    ).text

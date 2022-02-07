""" Script to generate list of urls to freeze in github actions.

Usage:
    source .env.dev
    python generate_urls.py

Outputs:
    urls_per_build_job.json: list of urls grouped for parallel build jobs
    build_job_ids.json: list of ids of build jobs
"""

import json
import math

from config import MAX_BUILD_JOBS, SITE_CONFIG
from helpers.api import fetch_gitub_database_tree


urls_per_build = 0
urls_per_build_job = []
freeze_candidates = []

# list of url prefix to ignore while freezing the site
exclude_url_prefix = [
    '/en/books/chanakya-neeti'
]


def get_site_urls():
    urls = ['/']
    urls += [f'/{language}/' for language in SITE_CONFIG['content_languages_codes']]
    return urls


def get_content_urls():
    urls = []

    github_database_tree = fetch_gitub_database_tree()
    languages = SITE_CONFIG['content_languages_codes']

    for language in languages:
        language_prefix = f'/{language}/'
        for node in github_database_tree['tree']:
            if node['type'] == 'tree':
                url = language_prefix + node['path'] + '/'
                if any(url.startswith(prefix) for prefix in exclude_url_prefix):
                    continue
                urls.append(url)
    return urls


freeze_candidates += get_site_urls()
freeze_candidates += get_content_urls()[:100]

urls_per_build = math.ceil(len(freeze_candidates) / MAX_BUILD_JOBS)

for i in range(0, len(freeze_candidates), urls_per_build):
    urls_per_build_job.append(
        freeze_candidates[i:i+urls_per_build]
    )

with open('urls_per_build_job.json', 'w') as urls_per_build_job_json:
    json.dump(urls_per_build_job, urls_per_build_job_json)
    print(f'saved urls_per_build_job.json')

with open('build_job_ids.json', 'w') as build_job_ids_json:
    build_job_ids = list(range(len(urls_per_build_job)))
    json.dump(build_job_ids, build_job_ids_json)
    print(f'saved build_job_ids.json')

print(f'Total URLs to freeze {len(freeze_candidates)}')

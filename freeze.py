import datetime
import math
import os
import shutil

from flask_frozen import Freezer
import threading

from app import app
from config import SITE_CONFIG
from helpers.api import fetch_gitub_database_tree

start_time = datetime.datetime.now()

app_root_path = app.root_path
build_destionation = 'build'
max_threads = 2
urls_frozen = 0


class URLFreezer():
    def __init__(self, urls, with_static_files=False):
        flask_app = app
        
        app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
        app.config['FREEZER_DESTINATION_IGNORE'] = ['*']
        app.config['FREEZER_DESTINATION'] = build_destionation
        app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html; charset=utf-8'
        app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
        app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
        app.config['FREEZER_SKIP_EXISTING'] = True
        
        self.urls = urls
        self.freezer = Freezer(flask_app, with_static_files)

    def yield_urls(self):
        for url in self.urls:
            print(f'freezing url {url}')
            global urls_frozen
            urls_frozen += 1
            yield url

    def freeze(self):
        self.freezer.register_generator(self.yield_urls)
        self.freezer.freeze()


def freeze_urls_asynchronous(urls, with_static_files, max_threads):
    urls_per_thread = math.ceil(len(urls) / max_threads)
    threads = []

    for i in range(0, len(urls), urls_per_thread):
        urls_chunk = urls[i:i+urls_per_thread]
        freezer = URLFreezer(urls_chunk, with_static_files)
        threads.append(
            threading.Thread(target=freezer.freeze)
        )

    print(f'Running {len(threads)} threads for {len(urls)}')

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def clean_build_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        os.mkdir(directory)


# list of urls to ignore while freezing the site
ignore_content_url_prefix = [
    '/en/books/chanakya-neeti'
]


def get_content_urls():
    urls = []

    github_database_tree = fetch_gitub_database_tree()
    languages = SITE_CONFIG['content_languages_codes']

    for language in languages:
        language_prefix = f'/{language}/'
        for node in github_database_tree['tree']:  # todo
            if node['type'] == 'tree':
                url = language_prefix + node['path'] + '/'
                if any(url.startswith(prefix) for prefix in ignore_content_url_prefix):
                    continue
                urls.append(url)
    return urls


def get_site_urls():
    urls = ['/']
    urls += [f'/{language}/' for language in SITE_CONFIG['content_languages_codes']]
    return urls


if __name__ == '__main__':
    clean_build_directory(build_destionation)

    site_urls = get_site_urls()
    content_urls = get_content_urls()

    total_url_count = len(site_urls) + len(content_urls)

    print(f'freezing {total_url_count} urls')

    # freeze website urls with static files
    freeze_urls_asynchronous(site_urls, with_static_files=True, max_threads=1)

    # freeze content urls without static files
    freeze_urls_asynchronous(
        content_urls, with_static_files=False, max_threads=max_threads)

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    days, seconds = duration.days, duration.seconds

    print(
        f'Generated static pages for {urls_frozen}/{total_url_count} urls in ' +
        f'{days * 24 + seconds // 3600}h:{(seconds % 3600) // 60}m:{seconds % 60}s '
    )

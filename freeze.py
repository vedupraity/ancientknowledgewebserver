import datetime
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
app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
app.config['FREEZER_DESTINATION_IGNORE'] = ['*']
app.config['FREEZER_DESTINATION'] = build_destionation
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html; charset=utf-8'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_SKIP_EXISTING'] = True
max_threads = 4

urls_frozen = 0


class freezerClass():
    def __init__(self, url, with_static_files):
        self.url = url
        self.freezer = Freezer(app, with_static_files)

    def _yield_urls(self):
        print(f'generating {self.url}')
        yield self.url

    def freeze(self):
        self.freezer.register_generator(self._yield_urls)
        self.freezer.freeze()


def freeze_single_url(url, with_static_files):
    freezer = freezerClass(url, with_static_files)
    freezer.freeze()


def freeze_urls_asynchronous(urls):
    threads = []

    for url in urls:
        global urls_frozen
        urls_frozen += 1
        threads.append(threading.Thread(
            target=freeze_single_url, args=(url, False,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def freeze_urls_synchronous(urls):
    for url in urls:
        global urls_frozen
        urls_frozen += 1
        freeze_single_url(url, True)


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
    freeze_urls_synchronous(site_urls)

    # freeze content urls without static files
    for i in range(0, len(content_urls), max_threads):
        _urls = content_urls[i:i+max_threads]
        freeze_urls_asynchronous(_urls)

    end_time = datetime.datetime.now()
    duration = end_time - start_time
    days, seconds = duration.days, duration.seconds

    print(
        f'Freeze ran for ' +
        f'{days * 24 + seconds // 3600}h:{(seconds % 3600) // 60}m:{seconds % 60}s ' +
        f'to freeze {urls_frozen} urls'
    )

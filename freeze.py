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
max_threads = 2

class freezerClass():
    def __init__(self, url):
        self.url = url
        self.freezer = Freezer(app)

    def _yield_urls(self):
        print(f'generating {self.url}')
        yield self.url

    def freeze(self):
        self.freezer.register_generator(self._yield_urls)
        self.freezer.freeze()


def freeze_single_url(url):
    freezer = freezerClass(url)
    freezer.freeze()


def freeze_urls_asynchronous(urls):
    threads = []

    for url in urls:
        threads.append(threading.Thread(
            target=freeze_single_url, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def freeze_urls_synchronous(urls):
    for url in urls:
        freeze_single_url(url)


def clean_build_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
        os.mkdir(directory)


def get_content_urls():
    urls = []
    
    github_database_tree = fetch_gitub_database_tree()
    languages = SITE_CONFIG['content_languages_codes']
    
    for language in languages:
        language_prefix = f'/{language}/'
        for node in github_database_tree['tree']:  # todo
            if node['type'] == 'tree':
                urls.append(language_prefix + node['path'] + '/')
    return urls


def get_urls_to_freeze():
    urls = ['/', '/about/', '/404/']
    urls += [f'/{language}/' for language in SITE_CONFIG['content_languages_codes']]
    urls += get_content_urls()
    return urls


if __name__ == '__main__':
    clean_build_directory(build_destionation)

    urls = list(set(get_urls_to_freeze()))
    print(f'freezing {len(urls)} urls')
    
    for i in range(0, len(urls), max_threads):
        _urls = urls[i:i+max_threads]
        freeze_urls_asynchronous(_urls)

    end_time = datetime.datetime.now()
    print(f'took {(end_time - start_time).seconds} seconds to freeze {len(urls)} urls')

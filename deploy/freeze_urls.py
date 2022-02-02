""" Script to freeze static files.

Usage:
    source .env.dev
    python freeze_urls.py 0

Outputs:
    build/: directory containing frozen html pages and static files
"""

import sys

from flask_frozen import Freezer

from app import app


app_root_path = app.root_path
build_destionation = 'build'
freeze_candidates = open('urls_per_build_job.json', 'r').read()
current_build_id = int(sys.argv[1])
freeze_with_static_files = True if current_build_id == 0 else False

app.config['FREEZER_REMOVE_EXTRA_FILES'] = False
app.config['FREEZER_DESTINATION_IGNORE'] = ['*']
app.config['FREEZER_DESTINATION'] = build_destionation
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html; charset=utf-8'
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_SKIP_EXISTING'] = True


def yield_urls():
    for url in freeze_candidates[current_build_id]:
        yield url


freezer = Freezer(app, with_static_files=freeze_with_static_files)
freezer.register_generator(yield_urls)
freezer.freeze()

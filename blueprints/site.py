from flask import Blueprint, render_template, url_for

from config import SITE_CONFIG
from helpers.api import get_yaml
from helpers.context import getBaseTemplateContext
from helpers.generic import get_meta_array

blueprint = Blueprint(f'website_blueprint', __name__)


@blueprint.route('/about/')
def aboutView():
    context = getBaseTemplateContext()
    context.update({
        'page_title': f'{SITE_CONFIG["site_title"]} | About',
        'page_description': SITE_CONFIG['site_description'],
    })

    return render_template(f'pages/about.html', **context)


@blueprint.route('/404/')
def pageNotFound():
    context = getBaseTemplateContext()

    return render_template(f'pages/404.html', **context)


@blueprint.route('/', defaults={'language': None})
@blueprint.route('/<language>/')
def homeView(language=None):
    supported_languages_code = [_[0] for _ in SITE_CONFIG['content_languages']]
    languages = [language] \
        if language in supported_languages_code else supported_languages_code

    books_meta = get_yaml('/books/meta.yaml')
    stotra_meta = get_yaml('/stotra/meta.yaml')

    context = getBaseTemplateContext()
    context.update({
        'books': list(get_meta_array(languages, books_meta, url_prefix='books')),
        'stotra': list(get_meta_array(languages, stotra_meta, url_prefix='stotra')),
    })

    return render_template(f'pages/home.html', **context)

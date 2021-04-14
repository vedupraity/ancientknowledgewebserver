from flask import Blueprint, render_template, url_for

from config import SITE_CONFIG
from helpers.api import RequestHelper
from helpers.context import getBaseTemplateContext


blueprint_name = 'home'

blueprint = Blueprint(f'{blueprint_name}_blueprint', __name__)


@blueprint.route('/')
def homeView():

    books_data_url = '/content/index.json'
    books_data = RequestHelper().getData(books_data_url)

    context = getBaseTemplateContext()
    context.update({
        'page_title': SITE_CONFIG['site_title'],
        'books': books_data,
    })

    return render_template(f'site/{blueprint_name}/index.html', **context)

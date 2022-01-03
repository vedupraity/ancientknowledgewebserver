from flask import Blueprint, render_template, url_for

from config import SITE_CONFIG
from helpers.api import RequestHelper
from helpers.context import getBaseTemplateContext


blueprint_name = 'home'

blueprint = Blueprint(f'{blueprint_name}_blueprint', __name__)


@blueprint.route('/')
def landingView():

    books_data_url = '/content/index.json'
    books_data = RequestHelper().getData(books_data_url)

    context = getBaseTemplateContext()
    context.update({
        'books': books_data,
    })

    return render_template(f'pages/landing.html', **context)

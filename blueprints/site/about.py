from flask import Blueprint, render_template, url_for

from config import SITE_CONFIG
from helpers.context import getBaseTemplateContext


blueprint_name = 'about'

blueprint = Blueprint(f'{blueprint_name}_blueprint', __name__)


@blueprint.route('/about/')
def aboutView():
    context = getBaseTemplateContext()
    context.update({
        'page_title': f'{SITE_CONFIG["site_title"]} | About',
        'page_description': SITE_CONFIG['site_description'],
    })

    return render_template(f'site/{blueprint_name}/index.html', **context)

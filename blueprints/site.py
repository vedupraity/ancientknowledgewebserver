from flask import Blueprint, render_template, request

from config import SITE_CONFIG
from helpers.api import get_yaml
from helpers.context import getBaseTemplateContext
from helpers.generic import get_meta_array

blueprint = Blueprint(f'website_blueprint', __name__)


@blueprint.route('/about/')
def aboutView():
    context = getBaseTemplateContext()
    context.update({
        'page_title': f'{SITE_CONFIG["site_title"]} | About Us',
        'page_url': SITE_CONFIG["site_url"] + request.path,
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
        
    content_root_meta = get_yaml(f'/meta.yaml')
    home_page_sections = []
    
    for root_meta_item in content_root_meta:
        _display_language = 'en' if len(languages) > 1 else languages[0]
        _id = root_meta_item['id']
        _name = root_meta_item['meta'][_display_language]['title']
        _meta_item = get_yaml(f'/{_id}/meta.yaml')
        cards = list(get_meta_array(languages, _meta_item, url_prefix=_id))
        
        home_page_sections.append({
            'name': _name,
            'url': f'/{_display_language}/{_id}/',
            'cards': cards
        })

    context = getBaseTemplateContext()
    context.update({
        'page_image': SITE_CONFIG["site_logo"],
        'page_url': SITE_CONFIG["site_url"] + request.path,
        'sections': home_page_sections,
    })

    return render_template(f'pages/home.html', **context)

from flask import Blueprint, render_template, url_for

from config import CONTENT
from helpers.api import RequestHelper
from helpers.breadcrumb import Breadcrumb
from helpers.context import getBaseTemplateContext
from helpers.pagination import Pagination


blueprint_name = 'bhagavad_gita_english'
blueprint = Blueprint(f'{blueprint_name}_blueprint', __name__)

page_title = CONTENT[blueprint_name]['page_title']
base_url = CONTENT[blueprint_name]['base_url']


@blueprint.route(f'/{base_url}/')
def bhagavadGitaEnglishIndexView():

    books_data_url = '/content/index.json'
    books_data = RequestHelper().getData(books_data_url)
    selected_book_meta = list(
        filter(lambda i: i['id'] == blueprint_name, books_data))[0]

    index_data_url = f'/content/{base_url}/index.json'
    index_data = RequestHelper().getData(index_data_url)

    breadcrumb = Breadcrumb()
    breadcrumb.add_items([
        {
            'page_name': selected_book_meta['title'],
            'page_url': '',
            'icon': 'fa-book',
            'active': True
        }
    ])

    context = getBaseTemplateContext()
    context.update({
        'blueprint_name': blueprint_name,
        'page_title': page_title,
        'site_image': selected_book_meta['coverImage'],
        'page_description': f'Read Shrimad Bhagavad Gita - As It Is in English.',
        'hero_title': selected_book_meta['title'],
        'breadcrumb': breadcrumb.data,
        'index_data': index_data,
    })

    return render_template(f'content/{blueprint_name}/index/index.html', **context)


@blueprint.route(f'/{base_url}/<chapter_id>/')
def bhagavadGitaEnglishChapterView(chapter_id):

    books_data_url = '/content/index.json'
    books_data = RequestHelper().getData(books_data_url)
    book_meta = list(
        filter(lambda i: i['id'] == blueprint_name, books_data))[0]

    index_data_url = f'/content/{base_url}/index.json'
    index_data = RequestHelper().getData(index_data_url)
    page_meta = list(filter(lambda i: i['id'] == chapter_id, index_data))[0]

    context = getBaseTemplateContext()

    breadcrumb = Breadcrumb()
    breadcrumb.add_items([
        {
            'page_name': book_meta['title'],
            'page_url': url_for(f'{blueprint_name}_blueprint.bhagavadGitaEnglishIndexView'),
            'breadcrumb': breadcrumb.data,
            'icon': 'fa-book',
            'active': False
        },
        {
            'page_name': page_meta['title'],
            'page_url': '',
            'icon': 'fa-file-alt',
            'active': True
        }
    ])

    if page_meta['isNested']:
        text_data = []

        for text_id in page_meta['pages']:
            post_data_url = f'/content/{base_url}/{chapter_id}/{text_id}/post.json'
            post_data = RequestHelper().getData(post_data_url)

            post_summary = ''
            for i, text in enumerate(post_data):
                if text['text'] == ['Translation']:
                    post_summary = post_data[i+1]['text']

            text_data.append({
                'id': text_id,
                'title': f'Chapter {chapter_id} - Verse {",".join(text_id.split("-"))}',
                'summary': post_summary
            })

        context.update({
            'blueprint_name': blueprint_name,
            'page_title': page_title,
            'site_image': book_meta['coverImage'],
            'page_description': f'Read Shrimad Bhagavad Gita - As It Is in English.',
            'hero_title': book_meta['title'],
            'breadcrumb': breadcrumb.data,
            'index_data': text_data,
        })

        return render_template(f'content/{blueprint_name}/index/index.html', **context)
    else:
        post_data_url = f'/content/{base_url}/{chapter_id}/post.json'
        post_data = RequestHelper().getData(post_data_url)

        context.update({
            'blueprint_name': blueprint_name,
            'page_title': page_title,
            'site_image': book_meta['coverImage'],
            'page_description': f'Read Shrimad Bhagavad Gita - As It Is in English.',
            'page_type': 'article',
            'hero_title': book_meta['title'],
            'breadcrumb': breadcrumb.data,
            'book_meta': book_meta,
            'page_meta': page_meta,
            'post_heading': page_meta['title'],
            'post_data': post_data,
        })

        return render_template(f'content/{blueprint_name}/post/index.html', **context)


@blueprint.route(f'/{base_url}/<chapter_id>/<text_id>/')
def bhagavadGitaEnglishTextView(chapter_id, text_id):

    books_data_url = '/content/index.json'
    books_data = RequestHelper().getData(books_data_url)
    book_meta = list(
        filter(lambda i: i['id'] == blueprint_name, books_data))[0]

    index_data_url = f'/content/{base_url}/index.json'
    index_data = RequestHelper().getData(index_data_url)
    page_meta = list(filter(lambda i: i['id'] == chapter_id, index_data))[0]

    context = getBaseTemplateContext()

    post_data_url = f'/content/{base_url}/{chapter_id}/{text_id}/post.json'
    post_data = RequestHelper().getData(post_data_url)

    breadcrumb = Breadcrumb()
    breadcrumb.add_items([
        {
            'page_name': book_meta['title'],
            'page_url': url_for(f'{blueprint_name}_blueprint.bhagavadGitaEnglishIndexView'),
            'breadcrumb': breadcrumb.data,
            'icon': 'fa-book',
            'active': False
        },
        {
            'page_name': page_meta['title'],
            'page_url': url_for(f'{blueprint_name}_blueprint.bhagavadGitaEnglishChapterView', chapter_id=chapter_id),
            'icon': 'fa-file-alt',
            'active': False
        },
        {
            'page_name': f'Verse {",".join(text_id.split("-"))}',
            'page_url': '',
            'icon': 'fa-quote-right',
            'active': True
        }
    ])

    context.update({
        'blueprint_name': blueprint_name,
        'page_title': page_title,
        'site_image': book_meta['coverImage'],
        'page_description': f'Read Shrimad Bhagavad Gita - As It Is in English. Chapter {chapter_id} - Verse {",".join(text_id.split("-"))}',
        'page_type': 'article',
        'hero_title': book_meta['title'],
        'breadcrumb': breadcrumb.data,
        'book_meta': book_meta,
        'page_meta': page_meta,
        'post_heading': f'Chapter {chapter_id} - Verse {",".join(text_id.split("-"))}',
        'post_data': post_data,
    })

    pagination = Pagination(
        all_pages=page_meta['pages'],
        current_page_id=text_id,
    )
    pagination.set_urls(
        first_page_url=url_for(f'{blueprint_name}_blueprint.bhagavadGitaEnglishTextView',
                               chapter_id=chapter_id, text_id=pagination.first_page['id']),
        last_page_url=url_for(f'{blueprint_name}_blueprint.bhagavadGitaEnglishTextView',
                              chapter_id=chapter_id, text_id=pagination.last_page['id']),
        previous_page_url=url_for(f'{blueprint_name}_blueprint.bhagavadGitaEnglishTextView', chapter_id=chapter_id,
                                  text_id=pagination.previous_page_id) if pagination.previous_page_id else None,
        next_page_url=url_for(f'{blueprint_name}_blueprint.bhagavadGitaEnglishTextView', chapter_id=chapter_id,
                              text_id=pagination.next_page_id) if pagination.next_page_id else None,
    )
    pagination.previous_button_text = "Previous Verse"
    pagination.next_button_text = "Next Verse"

    context.update({
        'is_paginated': True,
        'pagination': pagination
    })

    return render_template(f'content/{blueprint_name}/post/index.html', **context)
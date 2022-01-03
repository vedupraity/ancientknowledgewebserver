from flask import Blueprint, render_template, url_for
from ancientknowledgewebserver.config import SITE_CONFIG

from helpers.api import get_yaml, get_markdown
from helpers.context import getBaseTemplateContext
from helpers.generic import get_meta_object, get_meta_array, markdown_to_html


blueprint = Blueprint(f'content_blueprint', __name__)


def get_parent_metadata(language, path):
    parent_path = '/'.join(path.split('/')[:-1])
    parent_tree_metadata = get_yaml(f'/{parent_path}/meta.yaml')
    metadata = list(filter(lambda x: x['id'] == path.split(
        '/')[-1], parent_tree_metadata))[0]
    return get_meta_object(
        language,
        metadata,
        parent_path or path,
    )


def get_breadcrumb(language, content_path):
    breadcrumb = [{
        'name': 'Home',
        'path': f'/{language}/',
        'is_active': False,
        'icon_class': 'fas fa-home',
    }]

    for index in range(len(content_path.split('/'))):
        breadcrumb_path = '/'.join(content_path.split('/')[:index+1])
        content_path_metadata = get_parent_metadata(language, breadcrumb_path)

        breadcrumb.append({
            'name': content_path_metadata['title'],
            'path': f'/{language}/' + breadcrumb_path,
            'is_active': index == len(content_path.split('/')) - 1,
            'icon_class': 'fas fa-file-alt',
        })

    return breadcrumb


def get_tree_metadata(language, content_path):
    return list(get_meta_array(
        [language],
        get_yaml(f'/{content_path}/meta.yaml'),
        content_path,
    ))


def get_content(language, content_path):
    markdown_content = get_markdown(f'/{content_path}/{language}.md')
    return markdown_to_html(markdown_content)


def get_previous_page(language, current_path, breadcrumb_path_array):
    if current_path == breadcrumb_path_array[0]:
        return None

    parent_path = '/'.join(current_path.split('/')[:-1])
    parent_tree_meta = get_tree_metadata(language, parent_path)
    current_path_meta = list(filter(
        lambda x: x['id'] == current_path.split('/')[-1],
        parent_tree_meta,
    ))[0]
    current_path_meta_index_in_tree = parent_tree_meta.index(current_path_meta)

    if current_path_meta_index_in_tree == 0:
        # Step back recursively

        return get_previous_page(
            language,
            parent_path,
            breadcrumb_path_array,
        )
    else:
        # Step forward recursively
        new_current_path = parent_tree_meta[current_path_meta_index_in_tree -
                                            1]['path'].replace(f'/{language}/', '')
        new_current_path_meta = get_parent_metadata(language, new_current_path)

        if new_current_path_meta['type'] == 'leaf':
            return new_current_path_meta

        current_tree_meta = get_tree_metadata(
            language,
            parent_tree_meta[current_path_meta_index_in_tree -
                             1]['path'].replace(f'/{language}/', ''),
        )

        if current_path_meta['type'] == 'tree':
            previous_meta = current_tree_meta[-1]

            if previous_meta['type'] == 'leaf':
                return previous_meta

            return get_previous_page(
                language,
                previous_meta['path'].replace(f'/{language}/', ''),
                breadcrumb_path_array,
            )
        else:
            return current_path_meta


def get_next_page(language, current_path, breadcrumb_path_array):
    if current_path == breadcrumb_path_array[0]:
        return None

    parent_path = '/'.join(current_path.split('/')[:-1])
    parent_tree_meta = get_tree_metadata(language, parent_path)
    current_path_meta = list(filter(
        lambda x: x['id'] == current_path.split('/')[-1],
        parent_tree_meta,
    ))[0]
    current_path_meta_index_in_tree = parent_tree_meta.index(current_path_meta)

    if current_path_meta_index_in_tree == len(parent_tree_meta) - 1:
        # Step back recursively

        return get_next_page(
            language,
            parent_path,
            breadcrumb_path_array,
        )
    else:
        # Step forward recursively
        new_current_path = parent_tree_meta[current_path_meta_index_in_tree +
                                            1]['path'].replace(f'/{language}/', '')
        new_current_path_meta = get_parent_metadata(language, new_current_path)

        if new_current_path_meta['type'] == 'leaf':
            return new_current_path_meta

        current_tree_meta = get_tree_metadata(
            language,
            parent_tree_meta[current_path_meta_index_in_tree +
                             1]['path'].replace(f'/{language}/', ''),
        )

        if new_current_path_meta['type'] == 'tree':
            next_meta = current_tree_meta[0]

            if next_meta['type'] == 'leaf':
                return next_meta

            return get_next_page(
                language,
                next_meta['path'].replace(f'/{language}/', ''),
                breadcrumb_path_array,
            )
        else:
            return current_path_meta


def get_pagination(language, content_path, breadcrumb):
    breadcrumb_path_array = [_['path'].replace(
        f'/{language}/', '') for _ in breadcrumb][2:]

    return {
        'previous': get_previous_page(language, content_path, breadcrumb_path_array),
        'next': get_next_page(language, content_path, breadcrumb_path_array),
    }


def get_cover_image(language, breadcrumb):
    root_path = breadcrumb[2]['path'] if len(breadcrumb) > 2 else None
    default_cover_image = SITE_CONFIG['default_cover_image']
    
    if not root_path:
        return default_cover_image
    
    path_metadata = get_parent_metadata(
        language, root_path.replace(f'/{language}/', ''))

    if not path_metadata['image']:
        return default_cover_image
    else:
        return path_metadata['image']

def get_context(language, breadcrumb, parent_metadata, tree_metadata, content, pagination):
    context = getBaseTemplateContext()
    context.update({
        'breadcrumb': breadcrumb,
        'metadata': parent_metadata,
        'tree': tree_metadata,
        'content': content,
        'pagination': pagination,
        'cover_image': get_cover_image(language, breadcrumb),
    })
    return context


@blueprint.route('/<language>/<path:content_path>/')
def contentView(language, content_path):
    breadcrumb = get_breadcrumb(language, content_path)
    parent_metadata = get_parent_metadata(language, content_path)
    tree_metadata = get_tree_metadata(language, content_path) \
        if parent_metadata['type'] == 'tree' else None
    content = get_content(
        language, content_path) if parent_metadata['type'] == 'leaf' else None
    pagination = get_pagination(
        language, content_path, breadcrumb) if parent_metadata['paginated'] == True else None

    context = get_context(
        language,
        breadcrumb,
        parent_metadata,
        tree_metadata,
        content,
        pagination,
    )

    return render_template(f'pages/content.html', **context)

import markdown
import yaml


def yaml_to_json(yaml_content):
    return yaml.safe_load(yaml_content)


def get_meta_object(language, meta_item, url_prefix):
    _path_array = [language]
    if url_prefix:
        _path_array.append(url_prefix)
    _path_array.append(meta_item['id'])
    return {
        'id': meta_item['id'],
        'path': '/' + '/'.join(_path_array),
        'type': meta_item['type'],
        'paginated': meta_item['paginated'],
        'title': meta_item['meta'][language]['title'],
        'subtitle': meta_item['meta'][language]['subtitle'],
        'image': meta_item['meta'][language]['image'],
        'description_html': markdown_to_html(meta_item['meta'][language]['description']),
        'description_markdown': meta_item['meta'][language]['description'],
    } if language in meta_item['meta'] else None


def get_meta_array(languages: list, meta_objects: list, url_prefix: str):
    from app import thread_pool
    results = []

    for meta_item in meta_objects:
        for language in languages:
            # _meta = get_meta_object(language, meta_item, url_prefix)
            results.append(thread_pool.apply_async(
                get_meta_object,
                (language, meta_item, url_prefix)
            ))
    
    for result in results:
        _meta = result.get()
        if _meta:
            yield _meta


def markdown_to_html(markdown_content):
    return markdown.markdown(
        markdown_content,
        extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.smarty',
            'markdown.extensions.attr_list',
        ]
    )
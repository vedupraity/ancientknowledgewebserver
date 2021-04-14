from flask_frozen import Freezer, url_for

from app import app
from config import CONTENT
from helpers.api import RequestHelper


freezer = Freezer(app)

# bhagavad gita hindi - urls

bg_hindi_blueprint_name = 'bhagavad_gita_hindi'
bg_hindi_base_url = CONTENT[bg_hindi_blueprint_name]['base_url']

bg_hindi_index_url = f'/content/{bg_hindi_base_url}/index.json'
bg_hindi_index_data = RequestHelper().getData(bg_hindi_index_url)


@freezer.register_generator
def bhagavadGitaHindiChapterView():
    for chapter_meta in bg_hindi_index_data:
        chapter_id = chapter_meta['id']

        # yield {'chapter_id': chapter_id}
        yield url_for(
            f'{bg_hindi_blueprint_name}_blueprint.bhagavadGitaHindiChapterView',
            chapter_id=chapter_id
        )


@freezer.register_generator
def bhagavadGitaHindiTextView():
    for chapter_meta in bg_hindi_index_data:
        chapter_id = chapter_meta['id']
        if chapter_meta['isNested']:
            for text_id in chapter_meta['pages']:

                # yield {'chapter_id': chapter_id, 'text_id': text_id}
                yield url_for(
                    f'{bg_hindi_blueprint_name}_blueprint.bhagavadGitaHindiTextView',
                    chapter_id=chapter_id,
                    text_id=text_id
                )

# bhagavad gita english - urls


bg_english_blueprint_name = 'bhagavad_gita_english'
bg_english_base_url = CONTENT[bg_english_blueprint_name]['base_url']

bg_english_index_url = f'/content/{bg_english_base_url}/index.json'
bg_english_index_data = RequestHelper().getData(bg_english_index_url)


@freezer.register_generator
def bhagavadGitaEnglishChapterView():
    for chapter_meta in bg_english_index_data:
        chapter_id = chapter_meta['id']

        # yield {'chapter_id': chapter_id}
        yield url_for(
            f'{bg_english_blueprint_name}_blueprint.bhagavadGitaEnglishChapterView',
            chapter_id=chapter_id
        )


@freezer.register_generator
def bhagavadGitaEnglishTextView():
    for chapter_meta in bg_english_index_data:
        chapter_id = chapter_meta['id']
        if chapter_meta['isNested']:
            for text_id in chapter_meta['pages']:

                # yield {'chapter_id': chapter_id, 'text_id': text_id}
                yield url_for(
                    f'{bg_english_blueprint_name}_blueprint.bhagavadGitaEnglishTextView',
                    chapter_id=chapter_id,
                    text_id=text_id
                )


if __name__ == '__main__':
    freezer.freeze()

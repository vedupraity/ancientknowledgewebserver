from environs import Env
from flask import url_for


# Begin environment variables

env = Env()

ENV=env("ENV")
SITE_URL=env("SITE_URL")
DATABASE_URL=env("DATABASE_URL")

# End environment variables

# Begin site settings

SITE_CONFIG = {
    'site_title': 'Ancient Knowledge',
    'site_tagline': 'Recollecting the lost knowledge',
    'site_url': SITE_URL,  # 'https://www.ancientknowledge.in',
    'author_name': 'Vedprakash Upraity',
    'contact_email': 'ancientknowledgeinbox@gmail.com',
    'github_author_profile': 'https://github.com/vedupraity',
    'github_webserver_repo': 'https://github.com/vedupraity/ancientknowledgewebserver',
    'github_database_repo': 'https://github.com/vedupraity/ancientknowledgedatabase',
    'google_analytics_tracking_id': 'G-2G57C3C15V',
}

# End site settings

# Begin blueprint constants

CONTENT = {
    'bhagavad_gita_hindi': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Bhagavad Gita | Hindi',
        'base_url': 'bhagavad-gita-hindi',
    },
    'bhagavad_gita_english': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Bhagavad Gita | English',
        'base_url': 'bhagavad-gita-english',
    },
}

# End blueprint constants

from environs import Env
from flask import url_for


# Begin environment variables

env = Env()

ENV = env("ENV")
SITE_URL = env("SITE_URL")
DATABASE_URL = env("DATABASE_URL")

DATABASE_REPO_DIR = '/home/ved/Work/PersonalProjects/AncientKnowledge/ancientknowledgedatabase'

# End environment variables

# Begin site settings

SITE_CONFIG = {
    'env': ENV,
    'site_title': 'Ancient Knowledge',
    'site_tagline': 'Recollecting the lost knowledge',
    'site_description': 'An online library of Ancient Knowledge, Scriptures and Books about History, Philosophy, Spirituality, Religion and more.',
    'site_keywords': ['Ancient', 'Knowledge', 'India', 'History', 'Philosophy', 'Spirituality', 'Dharma', 'Religion', 'Sanatan', 'Hindu', 'Devotee'],
    'site_url': SITE_URL,
    'author_name': 'Vedprakash Upraity',
    'contact_email': 'ancientknowledgeinbox@gmail.com',
    'google_analytics_tracking_id': 'G-2G57C3C15V',
}

# End site settings

# Begin blueprint constants

CONTENT = {
    'bhagavad_gita_hindi': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Bhagavad Gita | Hindi',
        'base_url': 'bhagavad-gita-hindi',
        'keywords': ['Ancient', 'Knowledge', 'India', 'Shrimad', 'Bhagavad', 'Gita', 'Yatharoop', 'As It Is', 'Mahabharat', 'Krishna', 'Prabhupad', 'Hindi']
    },
    'bhagavad_gita_english': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Bhagavad Gita | English',
        'base_url': 'bhagavad-gita-english',
        'keywords': ['Ancient', 'Knowledge', 'India', 'Shrimad', 'Bhagavad', 'Gita', 'Yatharoop', 'As It Is', 'Mahabharat', 'Krishna', 'Prabhupad', 'English']
    },
    'ramcharitmanas_hindi': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Shriramcharitmanas | Hindi',
        'base_url': 'ramcharitmanas-hindi',
        'keywords': ['Ancient', 'Knowledge', 'India', 'Ramcharitmanas', 'Shriramcharitmanas', 'Hindi', 'Ram', 'Rama']
    },
    'ramcharitmanas_english': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Shriramcharitmanas | English',
        'base_url': 'ramcharitmanas-english',
        'keywords': ['Ancient', 'Knowledge', 'India', 'Ramcharitmanas', 'Shriramcharitmanas', 'English', 'Ram', 'Rama']
    },
}

# End blueprint constants

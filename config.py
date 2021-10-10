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
    'site_tagline': '“Our mission is to allow everyone to learn about Vedic Culture and the Sanatana Dharma.”',
    'site_description': 'An online library of Ancient Knowledge, Scriptures and Books about History, Philosophy, Spirituality, Religion and more.',
    'site_keywords': ['Ancient', 'Knowledge', 'India', 'History', 'Philosophy', 'Spirituality', 'Dharma', 'Religion', 'Sanatan', 'Hindu', 'Devotee'],
    'site_url': SITE_URL,
    'author_name': 'Vedprakash Upraity',
    'contact_email': 'ancientknowledgeinbox@gmail.com',
    'google_analytics_tracking_id': 'G-2G57C3C15V',
    'facebook_profile_url': 'https://www.facebook.com/PraacheenGyaan/',
    'instagram_profile_url': 'https://www.instagram.com/PraacheenGyaan/',
    'twitter_profile_url': 'https://www.twitter.com/PraacheenGyaan/',
}

# End site settings

# Begin blueprint constants

CONTENT = {
    'bhagavad_gita_hindi': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Bhagavad Gita | Hindi',
        'base_url': 'bhagavad-gita-hindi',
        'keywords': [
            'Ancient',
            'Knowledge',
            'India',
            'Shrimad',
            'Bhagavad',
            'Gita',
            'Yatharoop',
            'As It Is',
            'Mahabharat',
            'Krishna',
            'Prabhupad',
            'Hindi'
        ],
        'copyright_message': [
            'The BBT was established in 1972 by His Divine Grace A.C. Bhaktivedanta Swami Prabhupada, Founder-Acharya of the International Society for Krishna Consciousness. BBT is the publisher for his books. All material used here belongs to and copyrighted under BBT (Bhaktivedanta Book Trust).',
            '*“I specifically formed the BBT to invest in it exclusive rights for the printing of all literature containing my teachings, writings and lectures. In this way the collections are to be divided fifty percent for printing new books and fifty percent for construction of temples.”*',
            '– A.C. Bhaktivedanta Swami Prabhupada'
        ]
    },
    'bhagavad_gita_english': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Bhagavad Gita | English',
        'base_url': 'bhagavad-gita-english',
        'keywords': [
            'Ancient',
            'Knowledge',
            'India',
            'Shrimad',
            'Bhagavad',
            'Gita',
            'Yatharoop',
            'As It Is',
            'Mahabharat',
            'Krishna',
            'Prabhupad',
            'English'
        ],
        'copyright_message': [
            'The BBT was established in 1972 by His Divine Grace A.C. Bhaktivedanta Swami Prabhupada, Founder-Acharya of the International Society for Krishna Consciousness. BBT is the publisher for his books. All material used here belongs to and copyrighted under BBT (Bhaktivedanta Book Trust).',
            '*“I specifically formed the BBT to invest in it exclusive rights for the printing of all literature containing my teachings, writings and lectures. In this way the collections are to be divided fifty percent for printing new books and fifty percent for construction of temples.”*',
            '– A.C. Bhaktivedanta Swami Prabhupada'
        ],
    },
    'ramcharitmanas_hindi': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Shriramcharitmanas | Hindi',
        'base_url': 'ramcharitmanas-hindi',
        'keywords': [
            'Ancient',
            'Knowledge',
            'India',
            'Ramcharitmanas',
            'Shriramcharitmanas',
            'Hindi',
            'Ram',
            'Rama'
        ],
        'copyright_message': [
            'Material used on this page belongs to and copyrighted under Gitapress, Gorakhpur.'
        ],
    },
    'ramcharitmanas_english': {
        'page_title': f'{SITE_CONFIG["site_title"]} | Shriramcharitmanas | English',
        'base_url': 'ramcharitmanas-english',
        'keywords': [
            'Ancient',
            'Knowledge',
            'India',
            'Ramcharitmanas',
            'Shriramcharitmanas',
            'English',
            'Ram',
            'Rama'
        ],
        'copyright_message': [
            'Material used on this page belongs to and copyrighted under Gitapress, Gorakhpur.'
        ],
    },
}

# End blueprint constants

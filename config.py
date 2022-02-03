from environs import Env
from flask import url_for


# Begin environment variables

env = Env()

ENV = env("ENV")
SITE_URL = env("SITE_URL")
DATABASE_URL = env("DATABASE_URL")
GITHUB_DATABASE_BRANCH = env("GITHUB_DATABASE_BRANCH")
ENABLE_API_CACHE = env("ENABLE_API_CACHE")
THREAD_POOL_PROCESSES = int(env("THREAD_POOL_PROCESSES"))
MAX_BUILD_JOBS = int(env("MAX_BUILD_JOBS"))

DATABASE_REPO_DIR = '/home/ved/Work/PersonalProjects/AncientKnowledge/ancientknowledgedatabase'

# End environment variables

# Begin site settings

SITE_CONFIG = {
    'env': ENV,
    'site_url': SITE_URL,
    'site_title': 'Ancient Knowledge',
    'site_tagline': '“Our mission is to allow everyone to learn about Vedic Culture and the Sanātana Dharma.”',
    'site_tagline_short': '॥ धर्मो रक्षति रक्षितः ॥',
    'site_description': 'Free library of Texts, Scriptures and Books to learn the foundation of Sanātana Dharma.',
    'copyright_message': 'This website may contain Copyrighted material used under Fair Use (Section 107 of the Copyright Act) for personal research and non-profit educational purposes.',
    'site_logo': 'images/logo.png',
    'site_image': 'images/default-cover-4x3.jpg',
    'content_languages': [
        ('hi', 'Hindi'),
        ('en', 'English'),
    ],
    'site_locale_default': 'en_US',
    'site_locale_alternate': ['hi_IN'],
    'site_keywords': [
        'ancient', 'knowledge', 'india', 'sanatan', 'dharma', 'history', 'philosophy', 'spirituality', 'religion', 'hindu', 'devotee',
    ],
    'contact_email': 'ancientknowledgeinbox@gmail.com',
    'google_analytics_tracking_id': 'G-2G57C3C15V',
    'social_media_handle': 'PraacheenGyaan',
    'social_media_facebook': 'https://www.facebook.com/PraacheenGyaan/',
    'social_media_instagram': 'https://www.instagram.com/PraacheenGyaan/',
    'social_media_twitter': 'https://www.twitter.com/PraacheenGyaan/',
}

SITE_CONFIG['content_languages_codes'] = [_[0] for _ in SITE_CONFIG['content_languages']]

# End site settings

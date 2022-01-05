from environs import Env
from flask import url_for


# Begin environment variables

env = Env()

ENV = env("ENV")
SITE_URL = env("SITE_URL")
DATABASE_URL = env("DATABASE_URL")
GITHUB_DATABASE_BRANCH = env("GITHUB_DATABASE_BRANCH")

DATABASE_REPO_DIR = '/home/ved/Work/PersonalProjects/AncientKnowledge/ancientknowledgedatabase'

# End environment variables

# Begin site settings

SITE_CONFIG = {
    'env': ENV,
    'site_url': SITE_URL,
    'site_title': 'Ancient Knowledge',
    'site_tagline': '“Our mission is to allow everyone to learn about Vedic Culture and the Sanātana Dharma.”',
    'site_description': 'Free library of Ancient Knowledge from India including Texts, Scriptures and Books promoting the Sanātana Dharma.',
    'default_cover_image': 'images/default-cover-4x3.jpg',
    'content_languages': [
        ('hi', 'Hindi'),
        ('en', 'English'),
    ],
    'seo_keywords': [
        'ancient', 'knowledge', 'india', 'history', 'philosophy', 'spirituality', 'dharma', 'religion', 'sanatan', 'hindu', 'devotee',
    ],
    'contact_email': 'ancientknowledgeinbox@gmail.com',
    'google_analytics_tracking_id': 'G-2G57C3C15V',
    'social_media_facebook': 'https://www.facebook.com/PraacheenGyaan/',
    'social_media_instagram': 'https://www.instagram.com/PraacheenGyaan/',
    'social_media_twitter': 'https://www.twitter.com/PraacheenGyaan/',
}

SITE_CONFIG['content_languages_codes'] = [_[0] for _ in SITE_CONFIG['content_languages']]

# End site settings

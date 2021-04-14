from config import SITE_CONFIG, ENV


def getBaseTemplateContext():
    """ DO NOT OVERRIDE !!! """

    return {
        'env': ENV,
        'site_title': SITE_CONFIG['site_title'],
        'site_tagline': SITE_CONFIG['site_tagline'],
        'google_analytics_tracking_id': SITE_CONFIG['google_analytics_tracking_id'],
        'author_name': SITE_CONFIG['author_name'],
        'site_url': SITE_CONFIG['site_url'],
        'contact_email': SITE_CONFIG['contact_email'],
        'github_author_profile': SITE_CONFIG['github_author_profile'],
    }

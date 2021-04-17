from copy import copy

from config import SITE_CONFIG


def getBaseTemplateContext():

    return copy(SITE_CONFIG)


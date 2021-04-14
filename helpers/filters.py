def hindiNumeral(number):
    """ Convert to hindi numerals """
    mapper = {
        "0": "०",
        "1": "१",
        "2": "२",
        "3": "३",
        "4": "४",
        "5": "५",
        "6": "६",
        "7": "७",
        "8": "८",
        "9": "९"
    }

    number = str(number)

    hindi_number = ''

    for c in number:
        hindi_number += mapper[c] if c in mapper else c

    return hindi_number


FILTERS = [hindiNumeral]

def register_filters(app):
    """Register the template filters with an app instance"""
    for func in FILTERS:
        app.add_template_filter(func)
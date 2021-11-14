from flask import url_for


class Breadcrumb:
    def __init__(self):
        self.data = [
            {
                'page_name': 'Home',
                'page_url': url_for('home_blueprint.landingView'),
                'icon': 'fa-home',
                'active': False
            }
        ]
    
    def add_items(self, items):
        self.data += items

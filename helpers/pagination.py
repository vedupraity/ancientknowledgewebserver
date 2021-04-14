class Pagination:
    def __init__(self, all_pages, current_page_id):
        self.all_pages = all_pages
        self.current_page_id = current_page_id
        self.current_page_id_index = all_pages.index(current_page_id)

        self.previous_page_id = self.get_previous_page_id()
        self.next_page_id = self.get_next_page_id()

        self.is_first_page = self.previous_page_id == None
        self.is_last_page = self.next_page_id == None
        
        self.first_page = {
            'id': all_pages[0],
            'url': None,
        }
        self.last_page = {
            'id': all_pages[-1],
            'url': None,
        }
        self.current_page = {
            'id': current_page_id,
            'url': None,
        }
        self.previous_page = {
            'id': self.previous_page_id,
            'url': None,
        }
        self.next_page = {
            'id': self.next_page_id,
            'url': None,
        }
        self.render_previous_page_buttons = self.previous_page_id != None
        self.render_next_page_buttons = self.next_page_id != None
        self.render_previous_page_id_button = not(self.current_page_id_index < 2)
        self.render_next_page_id_button = not(len(all_pages) - self.current_page_id_index <= 2)
        self.render_previous_page_ellipsis = not(self.current_page_id_index < 3)
        self.render_next_page_ellipsis = not(len(all_pages) - self.current_page_id_index <= 3)
    
    def get_previous_page_id(self):
        if self.current_page_id_index == 0:
            return None
        return self.all_pages[self.current_page_id_index-1]

    def get_next_page_id(self):
        try:
            return self.all_pages[self.current_page_id_index+1]
        except:
            return None

    def set_urls(
        self,
        first_page_url,
        last_page_url,
        previous_page_url,
        next_page_url,
    ):
        self.first_page['url'] = first_page_url
        self.last_page['url'] = last_page_url
        self.previous_page['url'] = previous_page_url
        self.next_page['url'] = next_page_url



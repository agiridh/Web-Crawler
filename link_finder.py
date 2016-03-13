from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url  # like https://www.google.com
        self.page_url = page_url  # like https://www.google.com/images or https://www.google.com/mail
        self.links = set()  # contains all the links parsed by the crawler on a particular page


    def error(self, message):
        pass


    # In <a href = "https://www.google.com/images">, a: html tag, href: attribute, value: https://www.google.com
    # if the html tag is <a>, and if href is the attribute, add link to set
    # sometimes, href only has a relative url like: /images
    # so, parse.urljoin helps to add the base url to the relative url
    # the set self.links contains all the links on the page
    # a lot of data analytics can then be carried out on these links
    def handle_starttag(self, tag, attrs):

        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)


    def get_page_links(self):
        return self.links

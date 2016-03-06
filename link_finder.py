from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()


    def error(self, message):
        pass


    def handle_starttag(self, tag, attrs):
        print(tag)

find = LinkFinder()
find.feed("<html><head>This is a header</head><body>"
          "This is the body</body>></html>")
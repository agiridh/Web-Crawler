from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
import requests


##############
# NOTE: Found that in gather_links function
# using requests.get(url) to get html of a website works
# better than urlopen from the urllib.request module
##############


class Spider:
    # class variables - shared among all instances
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    # base_url, domain_name and project_name are user inputs
    def __init__(self, base_url, domain_name, project_name):

        Spider.base_url = base_url
        Spider.project_name = project_name
        Spider.domain_name = domain_name
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.queue_file = Spider.project_name + '/queue.txt'

        # run on a new project
        self.boot()
        self.crawl_page('First spider', Spider.base_url)


    # Creates a directory and creates files for the new website
    # Spider.queue_file only contains url of the homepage at this point
    @staticmethod
    def boot():
        create_new_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = add_filelines_to_set(Spider.queue_file)
        Spider.crawled = add_filelines_to_set(Spider.crawled_file)


    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print("{} now crawling {}".format(thread_name, page_url))
            print("Queue {} | Crawled {}".format(str(len(Spider.queue)), str(len(Spider.crawled))))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()


    # The linkfinder class takes in a string
    # The data returned by urlopen is in bytes
    # So, decode() helps us here. The output from decode() is passed to linkfinder which
    # returns a set of links
    # If a page doesn't have any links, return an empty set
    @staticmethod
    def gather_links(page_url):
        html_string = ''

        try:
            #response = urlopen(page_url)  # make sure we are connecting to an actual website
            #if response.getheader('Content-Type') == 'text/html':
            #    html_bytes = response.read()
            #    html_string = html_bytes.decode('utf-8')
            html_string = requests.get(page_url).text
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)

        except:
            print('Error: Cannot crawl page -  {}'.format(page_url))
            return set()

        return finder.get_page_links()


    @staticmethod
    def add_links_to_queue(links):

        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            # if there are links to other websites - YouTube or Facebook..etc, don't crawl them
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)


    @staticmethod
    def update_files():
        writing_set_to_file(Spider.queue, Spider.queue_file)
        writing_set_to_file(Spider.crawled, Spider.crawled_file)





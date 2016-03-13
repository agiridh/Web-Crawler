from urllib.request import urlopen
from link_finder import LinkFinder
from general import *


class Spider:
    # class variables - shared among all instances
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, base_url, domain_name, project_name):
        Spider.base_url = base_url
        Spider.project_name = project_name
        Spider.domain_name = domain_name
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.queue_file = Spider.project_name + '/queue.txt'
        self.boot()
        self.crawl_page('First spider', Spider.base_url)


    @staticmethod
    def boot():
        create_new_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = add_filelines_to_set(Spider.queue_file)
        Spider.crawled = add_filelines_to_set(Spider.crawled_file)

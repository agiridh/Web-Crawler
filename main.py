import threading
from queue import Queue
from spider import Spider
from general import *
from domain import *


# constants
PROJECT_NAME = 'thenewboston'
HOMEPAGE = 'https://www.thenewboston.com'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 7
queue = Queue()
Spider(HOMEPAGE, DOMAIN_NAME, PROJECT_NAME)

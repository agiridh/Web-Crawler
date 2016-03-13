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

# Run the first Worker/Spider
Spider(HOMEPAGE, DOMAIN_NAME, PROJECT_NAME)


# Create worker threads
# The argument related to the target is what the worker is supposed to do
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True  # will die when main exits
        t.start()



# Each queued link is a new job
def create_jobs():
    for link in add_filelines_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()  # when there are jobs available, no two threads fight to get the same job
    crawl()


# Check if there are items in queue.txt, if so, crawl em
def crawl():crea
    queued_links = add_filelines_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print("There are {} links in the queue.".format(str(len(queued_links))))
        create_jobs()




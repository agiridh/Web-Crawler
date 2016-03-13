## author: Aditya Giridhar
## This is a command line tool that crawls through all the links on a website
## More functionality could be added to this - some sort of data analytics maybe?
## Call syntax: python3 main.py

import threading
from queue import Queue
from spider import Spider
from general import *
from domain import *



def get_user_input():
    project_name = input("Enter name of project: ")
    homepage = input("Enter complete url of the homepage: ")
    number_of_threads = int(input("Enter the number of threads to use: "))
    domain_name = get_domain_name(homepage)

    return homepage, domain_name, project_name, number_of_threads


# Create worker threads
# The argument related to the target is what the worker is supposed to do
def create_workers(number_of_threads):
    for _ in range(number_of_threads):
        t = threading.Thread(target=work)
        t.daemon = True  # will die when main exits
        t.start()  # ask worker to start doing work


# Do next job in queue
def work():
    while True:
        url = queue.get()  # get url from queue.txt
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()  # end task for worker. It can now find more jobs, if available


# Each queued link is a new job
def create_jobs(queue_file):
    for link in add_filelines_to_set(queue_file):
        queue.put(link)
    queue.join()  # when there are jobs available, no two threads fight to get the same job
    crawl(queue_file)


# Check if there are items in queue.txt, if so, crawl em
def crawl(queue_file):
    queued_links = add_filelines_to_set(queue_file)
    if len(queued_links) > 0:
        print("There are {} links in the queue.".format(str(len(queued_links))))
        create_jobs(queue_file)


if __name__ == '__main__':

    homepage, domain_name, project_name, number_of_threads = get_user_input()
    queue_file = project_name + '/queue.txt'
    crawled_file = project_name + '/crawled.txt'
    queue = Queue()

    # Run the first Worker/Spider
    Spider(homepage, domain_name, project_name)

    create_workers(number_of_threads)
    crawl(queue_file)

import os

def create_new_dir(directory):
    if not os.path.exists(directory):
        print("Creating new project {}...".format(directory))
        os.makedirs(directory)

# create new file
def create_file(file, data):
    with open(file, 'w') as f:
        f.write(data)

# create queue and crawled files
# queue: consists of pages that have not been crawled
# crawled: consists of pages that have already been crawled
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        create_file(queue, base_url)
    if not os.path.isfile(crawled):
        create_file(crawled, base_url)


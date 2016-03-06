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


# Add another link to existing file
def append_data_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# write nothing onto file = deleting contents of file
def delete_file_content(path):
    with open(path, 'w'):
        pass


# File I/O is a bottleneck in a program that crawls through thousands
# of web pages. So, it is better to write those crawled website links to a set
# this function stores each line of file in a set
def add_filelines_to_set(file):
    with open(file, 'rt') as f:
        results = set()
        for line in file:
            results.add(line.replace("\n", ""))

    return results


# each item of set will be a new line in the file
def writing_set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_data_to_file(file, link)
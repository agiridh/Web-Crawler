import os

def create_new_dir(directory):
    if not os.path.exists(directory):
        print("Creating new project {}...".format(directory))
        os.makedirs(directory)

create_new_dir("google")
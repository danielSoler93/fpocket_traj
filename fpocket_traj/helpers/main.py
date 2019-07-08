import os
import shutil


class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)


def create_dir(directory):
    if os.path.exists(directory):
        pass
    else:
        os.mkdir(directory)


def remove(input_file, copy, directory="snapshots_copy"):
    if copy:
        create_dir(directory)
        shutil.copy(input_file, directory)
    if not os.path.exists(input_file):
        pass
    else:
        os.remove(input_file)


def remove_dir(directory):
    if not os.path.exists(directory):
        pass
    else:
        shutil.rmtree(directory)


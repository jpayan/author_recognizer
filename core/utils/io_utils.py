from os import listdir
from os.path import isfile, join
from pickle import dump, load, HIGHEST_PROTOCOL


BEGIN = '<s>'
END = '</s>'


def open_file(file, mode):
    return open(file, mode, encoding='utf-8')


def save_object(obj, file_name):
    with open(file_name, 'wb') as file:
        dump(obj, file, HIGHEST_PROTOCOL)


def load_object(file_name):
    with open(file_name, 'rb') as file:
        return load(file)


def get_dir_files(dir_path):
    return [file for file in listdir(dir_path) if isfile(join(dir_path, file))]

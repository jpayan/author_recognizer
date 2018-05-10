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

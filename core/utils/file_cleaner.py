import re
from os import listdir
from os.path import isfile, join


def get_dir_files(dir_path):
    return [file for file in listdir(dir_path) if isfile(join(dir_path, file))]


if __name__ == '__main__':
    dir_path = '../../training/Shakespeare'
    files = get_dir_files(dir_path)

    for file in files:
        file_path = join(dir_path, file)

        lines = []
        with open(file_path, 'r', encoding='utf8') as stream:
            lines = stream.readlines()
            for line in lines:
                re.sub(r'^<.*>$', '', line)

        with open(file_path, 'w') as stream:
            stream.write(lines)

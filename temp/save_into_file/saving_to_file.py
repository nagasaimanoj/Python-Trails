from os.path import dirname
from pickle import dump

data = {
    'name': 'manoj',
    'age': 23
}

file_name = dirname(__file__)+'/sample_pickle_file'
file_handler = open(file_name, 'wb')

dump(data, file_handler)

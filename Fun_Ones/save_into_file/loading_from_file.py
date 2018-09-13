from pickle import load

file_name = 'sample_pickle_file'
file_handler = open(file_name, 'rb')

data = load(file_handler)

print(data)

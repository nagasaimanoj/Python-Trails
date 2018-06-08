import json

# using python dictionary
sample_dict = {"name": "manoj", "age": 22}
print("dictionary = ", sample_dict)

json_dist = json.dumps(sample_dict)
print("json from distionary = ", json_dist)

sample_dict_2 = json.loads(json_dist)
print("un-json'ng dist = ", sample_dict_2)

# using python tuple
sample_tup = (1, 2, 3, 4, 5, 6)
print("tuple =", sample_tup)

json_tup = json.dumps(sample_tup)
print("json from tuple =", json_tup)

sample_tup_2 = json.loads(json_tup)
print("un-json'ng tup = ", sample_tup_2)

# using python list
sample_list = [10, 20, 30, 40, 50]
print("list =", sample_list)

json_list = json.dumps(sample_list)
print("json from list =", json_list)

sample_list_2 = json.loads(json_list)
print("un-json'ng list = ", sample_list_2)

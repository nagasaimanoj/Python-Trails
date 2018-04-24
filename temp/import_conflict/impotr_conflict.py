import os, imp

for description in imp.get_suffixes():
    abs_path = os.path.dirname(__file__)
    imp.load_module("pkg", open(abs_path), abs_path, (description))

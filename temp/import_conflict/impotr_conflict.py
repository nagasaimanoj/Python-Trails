import os, imp


def import_module(dir, name):
    """ load a module (not a package) with a given name 
        from the specified directory 
    """
    for description in imp.get_suffixes():
        (suffix, mode, type) = description
        if not suffix.startswith('.py'): continue
        abs_path = os.path.join(dir, name + suffix)
        if not os.path.exists(abs_path): continue
        fh = open(abs_path)
        return imp.load_module(name, fh, abs_path, (description))


import_module('.', 'pkg')
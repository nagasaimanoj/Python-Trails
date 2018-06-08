def import_or_install(package):
    from importlib import import_module
    try:
        import_module(package)
        print(package, "already installed")
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = import_module(package)


import_or_install('transliterate')

from yaml import safe_load

config_file = open('config.yaml')

dataMap = safe_load(config_file)

print(dataMap)

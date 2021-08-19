import json

def nested_set(dic, keys, value): # https://stackoverflow.com/a/13688108/14345173
    for key in keys[:-1]:
        dic = dic.setdefault(key, {})
    dic[keys[-1]] = value

def load():
    parsed_config_data = json.load(open('src/config.yml'))
    return parsed_config_data

def edit(path, to: str):
    if isinstance(path, str):
        path = [path]

    source = load()
    nested_set(source, path, to)

    json.dump(data=source, stream=open('src/config.yml', 'w'), indent=4)

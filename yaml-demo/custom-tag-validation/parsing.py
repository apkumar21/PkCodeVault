import yaml

with open("parsing.yaml", "r") as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as e:
        print(e)

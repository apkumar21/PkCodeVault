import yaml

def constructor(loader, node):
    fields = loader.construct_mapping(node)
    return Person(**fields)

yaml.add_constructor('!Person', constructor)

class Person(object):
    
    def __init__(self, name, age):
        self.name = name;
        self.age = age

with open("/Users/e177305/my-projects/PythonPioneers/yaml-demo/standard-validation/custom-tag.yaml","r") as stream:
    try:
        dict_person = yaml.unsafe_load(stream)
        print(dict_person)
        person = dict_person["person"]
        print(person.name, person.age)
    except yaml.YAMLError as e: 
        print(e)
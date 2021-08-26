
import yaml
from configparser import ConfigParser
import json
import os
# relative_path = r'\python_handson\nfs.example.lan.yml'
# path = os.path.join(sf.data_path,relative_path)
relative_path = 'nfs.example.lan.yml'
path = r'C:\Users\ankit.chandel\Desktop\python_handson\nfs.example.lan.yml'
with open(relative_path, 'r') as stream:
    try:
        yaml_content = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
# write the .yaml file into the .json file
with open('sample.json','w') as out_file:
    json.dump(yaml_content,out_file,indent=4)


# for reading .config/.conf/.ini files
config = ConfigParser()
print(config.sections())

config.read("config.ini")
config.read("sampleconf.conf")
config.read("sample_client.txt")
print(config.sections())







    
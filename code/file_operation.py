# read 
# The module should be able to read .yaml, .cfg, .conf configuration file formats, 
# read the configurations and generate a flat dictionary out of it.
import yaml
from configparser import ConfigParser
import json
import os
relative_path = 'nfs.example.lan.yml'
# path = os.path.join(sf.data_path,relative_path)
relative_path = 'nfs.example.lan.yml'
path = r'C:\Users\ankit.chandel\Desktop\python_handson\nfs.example.lan.yml'
with open(path, 'r') as stream:
    try:
        yaml_content = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
# write the .yaml file into the .json file
with open('sample.json','w') as out_file:
    json.dump(yaml_content,out_file,indent=4)






config = ConfigParser()
parser = config.read("dev.ini")
print(parser)  # ['settings', 'db', 'files']
# print(parser.get('settings', 'secret_key'))  # abc123
# print(parser.options('settings'))  # ['debug', 'secret_key', 'log_path']


# print('db' in parser)  # True

# option_values = parser.get("your-config", "path1")
# print(json.load(parser_onj))


# # read conf file 
# config = configparser.ConfigParser()
# print(config.read('sampleconfig.conf'))
# # print(conf_obj)


    
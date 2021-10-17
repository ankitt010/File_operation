
import yaml
from configparser import ConfigParser
import json
import os
from ankit import hi
from .
# import file
# some_file.py
import sys

# insert at 1, 0 is the script path (or '' in REPL)C:\Users\ankit.chandel\Desktop\python_handson\new_folder
# new_folder
# sys.path.insert(1, r'C:\Users\ankit.chandel\Desktop\python_handson\new_folder')
sys.path.append(r'C:\Users\ankit.chandel\Desktop\python_handson\new_folder')
# from new_folder.new import 

# import_path = __import__('new-folder') 



# relative_path = r'\python_handson\nfs.example.lan.yml'
# path = os.path.join(sf.data_path,relative_path)
relative_path = 'nfs.example.lan.yml'
# path = r'C:\Users\ankit.chandel\Desktop\python_handson\nfs.example.lan.yml'
with open(relative_path, 'r') as stream:
    try:
        yaml_content = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
# write the .yaml file into the .json file
with open('sample.json','w') as out_file:
    json.dump(yaml_content,out_file,indent=4)


# for reading .config/.conf/.ini files
# ConfigParser is the library from where we can parse these key-value based files.
config = ConfigParser()
print(config.sections())

config.read("config.ini")  #using config object reading the .ini file

print(config.sections())








    
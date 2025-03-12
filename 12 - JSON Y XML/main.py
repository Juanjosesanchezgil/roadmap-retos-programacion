import xml.etree.ElementTree as xml
import json
import os

data = {
    "name": "Juan Sanchez",
    "age": 40,
    "birth_date": "29-05-1984",
    "programming_languages": ["Python", "Kotlin", "Swift"]
}

xml_file = "juan.xml"
json_file = "juan.json"

def create_xml():
    with open(xml_file, "w") as xml_data:
        

def create_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)


create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())


os.remove(json_file)

import openpyxl
import json
from itens import Municipio
from itens import JsonRegioes

def obj_dict(obj):
    return obj.__dict__

mun1 = Municipio(1,'salvador',13,123123,'lol',[1,2,3,4],[1,2,9,20],12,13)
mun2 = Municipio(2,'abaira',13,3123,'lol',[1,2,3,4],[5,6,7,8],12,13)
mun3 = Municipio(2,'abaira',13,3123,'lol',[1,2,3,4],[0,500,0,500],12,13)

j = JsonRegioes()

j.add_item("MUNICIPIOS",mun1)
j.add_item("MUNICIPIOS",mun2)
j.add_item("MUNICIPIOS",mun3)

s = json.dumps(j.get_itens(), default=obj_dict)

try:
    # Get a file object with write permission.

    text_file = open("Output.json", "w")
    text_file.write("%s" % s)
    text_file.close()

    print('./a.json' + " created. ")
except FileNotFoundError:
    print('./a.json' + " not found. ")

print(s)
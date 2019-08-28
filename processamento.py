import xlrd
import json
from itens import Municipio
from itens import JsonRegioes

def obj_dict(obj):
    return obj.__dict__

estados = ['Bahia']
proc_flag = False

wb = xlrd.open_workbook('./2010/abacate.xls', formatting_info=True)

sheet = wb.sheet_by_index(0)

for i in range(sheet.nrows):
    cell = sheet.cell(i,0)
    inf = wb.xf_list[cell.xf_index]
    if(inf.alignment.indent_level == 0):
        if(not proc_flag and cell.value in estados):
            proc_flag = True
        else:
            proc_flag = False
    if(proc_flag):
        print(cell.value)
        print(inf.alignment.indent_level)

mun1 = Municipio(1,'salvador',13,123123,'lol',[1,2,3,4],[1,2,9,20],12,13)
mun2 = Municipio(2,'abaira',13,3123,'lol',[1,2,3,4],[5,6,7,8],12,13)
mun3 = Municipio(3,'abaira',13,3123,'lol',[1,2,3,4],[0,500,0,500],12,13)

j = JsonRegioes()

j.add_item("MUNICIPIOS",mun1)
j.add_item("MUNICIPIOS",mun2)
j.add_item("MUNICIPIOS",mun3)

s = json.dumps(j.get_itens(), default=obj_dict)

try:
    text_file = open("Output.json", "w")
    text_file.write("%s" % s)
    text_file.close()

    print("Json criado.")
except FileNotFoundError:
    print("Json não criado, arquivo não encontrado")
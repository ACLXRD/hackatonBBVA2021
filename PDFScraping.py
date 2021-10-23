import tabula as tb
import pandas as pd
from  PyPDF2 import PdfFileReader 
import re
import os
# from tabulate import tabulate

#LECTURA DE LA PAGINA 1
urlPDF=r'C:\Users\Felipe Velasquez\Dropbox\My PC (DESKTOP-1LIROPU)\Documents\Octavo Semestre 2021\Hackaton\RUT3.pdf'
data = tb.read_pdf(urlPDF, pages = '1',pandas_options={'header': None}, stream=True)[0]
# data.to_csv('file_name.csv')

#Numero de paginas del PDF
with open(urlPDF, "rb") as filehandle:
    pdf = PdfFileReader(filehandle)
    pages = pdf.getNumPages()

# Scraping to NIT
nit=[]
for i in range(3):
    iter=data[i][5]
    nit+=iter
    nit="".join(nit).replace(" ", "")

# #Scraping to Tipo de persona
tipoPersona=data[0][8]

# Scraping to razon social
razonSocial=data[0][13]

#Scraping to pais
pais=data[0][18]

#Scraping to Departamento
dept=''.join([i for i in data[4][18] if not i.isdigit()])
codDept=''.join([i for i in data[6][18] if  i.isdigit()])

#Scraping to Municipio
municipio=''.join([i for i in data[6][18] if not i.isdigit()])
codMun=str(int(data[11][18])) +str(int(data[12][18]))+ str(int(data[13][18]))

#Scraping to direccion
dir=data[0][20]

#Scraping to email
correo=data[0][22]

#Scraping to codigo de actividad economica
actividad=data[0][28].split()
codActividad=[]
for i in range(4):codActividad+=actividad[i]
codActividad="".join(codActividad).replace(" ", "")

#Scraping to fecha de inicio de actividad economica
año=actividad[4]+actividad[5]+actividad[6]+actividad[7]
año="".join(año).replace(" ", "")

mes=actividad[8]+actividad[9]
mes="".join(mes).replace(" ", "")

dia=actividad[10]+actividad[11]
dia="".join(dia).replace(" ", "")

fechaInicioAct=f'{año}/{mes}/{dia}'

#Scraping to telefono
tel=data[6][22]+data[7][22]
tel="".join(tel).replace(" ", "")

data = tb.read_pdf(urlPDF, pages = '2',pandas_options={'header': None}, stream=True)[0]
# data.to_csv('file_name.csv')


# #Scraping to Fecha de registro
fecha=[]
for i in range(5): 
    fecha+=str(data[i][24])
fecha=''.join([i for i in fecha if i.isdigit()])
año=fecha[2]+fecha[3]+fecha[4]+fecha[5]
mes=fecha[6]+fecha[7]
dia=fecha[8]+fecha[9]
fechaRegistro=f'{año}/{mes}/{dia}'

#Scraping to Matricula mercantil
row=[]
for i in range(5):
    row+=str(data[i][20])
row=row[29]+row[31]+row[32]+row[33]+row[34]+row[35]+row[37]+row[39]
nMatricula=row

data = tb.read_pdf(urlPDF, pages = '3',pandas_options={'header': None}, stream=True)[0]
data.to_csv('file_name.csv')

#Scrapping to tipo  C.C.
tipoDocRepresentante=''.join([i for i in data[0][11] if not i.isdigit()])

#Scraping to Numero de documento del representante
ccRepresentante=[]
for i in range(10):ccRepresentante+=str(data[i][11])
ccRepresentante=''.join([i for i in ccRepresentante if  i.isdigit()])


#Scrapping to nombre del representante
primerNombre=data[5][14]
Segundonombre=data[8][14]
primerApellido=data[0][14]
segundoApellido=data[2][14]



# #Scraping to C.C.
# row=data[10][7]
# cc=[]
# for i in row:
#     if i!=' ':
#         cc.append(i)
# cc.pop(0);cc.pop(0)
# cc="".join(cc)

# #Scraping to fecha exp
# row=data[14][7]
# print(row,data[15][7])
# print('PAGINA 1')
# print('El nit es ',nit)
# print('El tipo de persona  es ',tipoPersona)
# print('la razon social es ',razonSocial)
# print('Esta ubicada en ',pais,' ',dept,' ',municipio,' ')
# print('el codigo del departamento es ',codDept)
# print('el codigo del municicipo es ',codMun)
# print('la direccion es ',dir)
# print('el correo es ',correo)
# print('el telefono es ',tel)
# print('el codigo de la actividad economica es ',codActividad)
# print('el inicio de la actividad economica fue ',fechaInicioAct)
# print('\n PAGINA 2')
# print('la fecha de registro es ',fechaRegistro)
# print('el numero de matricula es ',nMatricula)

print('\n PAGINA 3')
print('La el tipo de documento del representante es ',tipoDocRepresentante)
print('La ceduladel representante es ',ccRepresentante)
print('El nombre del representante es ', primerApellido,segundoApellido,primerNombre,Segundonombre)
import tabula as tb
import pandas as pd
from  PyPDF2 import PdfFileReader 
import re
import os
import json

def getInfoBasic(urlPDF):
    data = tb.read_pdf(urlPDF, pages = '1',pandas_options={'header': None}, stream=True)[0]
    # data.to_csv('file_name.csv')
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

    datos={'NIT':nit,'tipoPersona':tipoPersona,'razonSocial':razonSocial,'pais':pais,'codDept':codDept,
        'departamento':dept,'codMunicipio':codMun,'direccion':dir,'correo':correo,'codActividad':codActividad,
        'fechaInicioActividad':fechaInicioAct,'telefono':tel}
    return datos


def getCaracteristicas(urlPDF):
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

    datos={'fechaRegistro':fechaRegistro,'numeroMatricula':nMatricula}
    return datos


def getInfoRepresentante(urlPDF):
    data = tb.read_pdf(urlPDF, pages = '3',pandas_options={'header': None}, stream=True)[0]
    # data.to_csv('file_name.csv')

    #Scrapping to tipo  C.C. del representante
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

    datos={'tipoDocumento':tipoDocRepresentante,'numeroDocumento':ccRepresentante,'primernombre':primerNombre,
    'segundoNombre':Segundonombre,'primerApellido':primerApellido,'segundoApellido':segundoApellido}
    return datos


def getInfoSocios(urlPDF):
    datos=[]
    for i in range(3):
        data = tb.read_pdf(urlPDF, pages = str(4+i),pandas_options={'header': None}, stream=True)[0]
        print(i)
        ult=0
        if i==2: ult=1
        for socio in range(5):
            try:
                tipoDocSocio=''.join([i for i in data[0][(8)*(socio+1)+ult] if not str(i).isdigit()])
                #Scraping to Numero de documento del Socio
                ccSocio=[]
                for i in range(10):ccSocio+=str(data[i][(8+ult)*(socio+1)])
                ccSocio=''.join([i for i in ccSocio if  i.isdigit()])

                #Scrapping to nombre del Socio
                row=(10+ult)+(socio*8)
                primerNombreS=data[6][row]
                SegundonombreS=data[7][row]
                primerapellidoS=data[0][row]
                SegundoapellidoS=data[2][row]
                if ccSocio=="":
                    break;
                iter={'tipoDocumentoSocio':tipoDocSocio,'numeroDocumentoSocio':ccSocio,'primernombre':primerNombreS,
                'segundoNombre':SegundonombreS,'primerApellido':primerapellidoS,'segundoApellido':SegundoapellidoS}
                datos.append(iter)
            except:
                print("no hay mas socios")
        return datos

print('hola')
urlPDF=r'C:\Users\Felipe Velasquez\Dropbox\My PC (DESKTOP-1LIROPU)\Documents\Octavo Semestre 2021\Hackaton\RUT3.pdf'    
print(getInfoBasic(urlPDF))
print(getCaracteristicas(urlPDF))
print(getInfoRepresentante(urlPDF))
print(getInfoSocios(urlPDF))
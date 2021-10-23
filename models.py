class Cliente():
    def __init__(self,id,nit,nombreComercial,razonSocial,sigla,codigoOcupacion,direccion,codigoPostal,correo,establecimientos,firma,frase,municipio,documento,tipoPersona,telefonos):
        self.id=id
        self.nit=nit
        self.nombreComercial=nombreComercial
        self.razonSocial=razonSocial
        self.sigla=sigla
        self.codigoOcupacion=codigoOcupacion
        self.direccion=direccion
        self.codigoPostal=codigoPostal
        self.correo=correo
        self.establecimientos=establecimientos
        self.firma=firma
        self.frase=frase
        self.municipio=municipio
        self.documento=documento
        self.tipoPersona=tipoPersona
        self.telefonos=telefonos

class Departamento():
    def __init__(self,id,nombre):
        self.id=id
        self.nombre=nombre

class Municipio():
    def __init__(self,id,nombre,departamento):
        self.id=id
        self.nombre=nombre
        self.departamento=departamento

class Documento():
    def __init__(self,numero,fechaExpedicion,tipoDocumento,municipio):
        self.numero=numero
        self.fechaExpedicion=fechaExpedicion
        self.tipoDocumento=tipoDocumento
        self.municipio=municipio

class Telefono():
    def __init__(self,id,numero):
        self.id = id
        self.numero = numero

class TipoDocumento():
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

class TipoPersona():
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

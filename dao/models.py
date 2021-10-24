import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

class Cliente(Object):
    """Clients model"""
    def __init__(self,id=0,nit=0,nombreComercial=0,
    razonSocial="",sigla=0,direccion="",correo="",establecimientos=0,
    firma="",frase="",rut="",municipio=0,tipoPersona="",telefonos=[],
    socios=[],representantes=[],actividades=[],token=""):
        self.id=id
        self.nit=nit
        self.nombreComercial=nombreComercial
        self.razonSocial=razonSocial
        self.sigla=sigla
        self.direccion=direccion
        self.correo=correo
        self.establecimientos=establecimientos
        self.firma=firma
        self.frase=frase
        self.municipio=municipio
        self.tipoPersona=tipoPersona
        self.telefonos=telefonos
        self.socios=socios
        self.representantes=representantes
        self.actividades=actividades
        self.rut=rut
        self.token=token

class Departamento(Object):
    """Departments model"""
    def __init__(self,id,nombre):
        self.id=id
        self.nombre=nombre

class Municipio(Object):
    """Municipality model"""
    def __init__(self,id,nombre,departamento):
        self.id=id
        self.nombre=nombre
        self.departamento=departamento

class Documento(Object):
    """Documents model"""
    def __init__(self,numero,fechaExpedicion,tipoDocumento,municipio):
        self.numero=numero
        self.fechaExpedicion=fechaExpedicion
        self.tipoDocumento=tipoDocumento
        self.municipio=municipio

class Telefono(Object):
    """Phones model"""
    def __init__(self,id,numero):
        self.id = id
        self.numero = numero

class TipoDocumento(Object):
    """Kind documents model"""
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

class TipoPersona(Object):
    """Kind persons model"""
    def __init__(self,id,tipo):
        self.id = id
        self.tipo = tipo

class Persona(Object):
    """Persona model"""
    def __init__(self,id,primerNombre,segundoNombre,primerApellido,segundoApellido,documento,nacionalidad):
        self.id=id
        self.primerNombre=primerNombre
        self.segundoNombre=segundoNombre
        self.primerApellido=primerApellido
        self.segundoApellido=segundoApellido
        self.documento=documento
        self.nacionalidad=nacionalidad

class Representante(Persona):
    def __init__(self,id,primerNombre,segundoNombre,primerApellido,segundoApellido,documento,nacionalidad,inicioRepresentacion):
        super(Representante,self).__init__(id,primerNombre,segundoNombre,primerApellido,segundoApellido,documento,nacionalidad)
        self.inicioRepresentacion=inicioRepresentacion

class Socio(Persona):
    def __init__(self,id,primerNombre,segundoNombre,primerApellido,segundoApellido,documento,nacionalidad,ingreso):
        super(Representante,self).__init__(id,primerNombre,segundoNombre,primerApellido,segundoApellido,documento,nacionalidad)
        self.ingreso=ingreso


class Actividad(Object):
    def __init__(self,codigo,inicio,cliente):
        self.codigo=codigo
        self.inicio=inicio
        self.cliente=cliente

class Balance(Object):
    def __init__(self,cliente_id,activos,pasivos,patrimonio):
        self.cliente_id=cliente_id
        self.activos=activos
        self.pasivos=pasivos
        self.patrimonio=patrimonio

class Nacionalidad(Object):
    """Kind persons model"""
    def __init__(self,id,nacionalidad):
        self.id = id
        self.nacionalidad = nacionalidad
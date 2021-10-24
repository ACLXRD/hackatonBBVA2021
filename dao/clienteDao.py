from dao import *
from models import *
class ClienteDao(DAO):
    def crear(self,cliente):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "insert into cliente (token,frase) values ('"+cliente.token+"');"
            cursor.execute(sql)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False
    def consultarPorToken(self,token):
        """ Se consultan datos de un usuario mediante su token
        Parámetros:

        - token--- que es el token de usuario
        """
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from cliente where token='"+token+"';"
            cursor.execute(sql)
            cliente=None
            for row in cursor:
                cliente = Cliente(id=row[0],
                nit=row[1],
                nombreComercial=row[2],
                razonSocial=row[3],
                sigla=row[4],
                direccion=row[5],
                correo=row[6],
                establecimientos=row[7],
                firma=row[8],
                frase=row[9],
                rut=row[10],
                municipio=row[11],
                tipoPersona=row[12])
            cursor.close()
            cnx.close()
            return cliente
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

from application.config import CONFIG
import pymysql

config = CONFIG["DATABASE"]

def getConexion():
    return pymysql.connect(host=config["HOST"],
                                user=config["USER"],
                                password=config["PASSWORD"],
                                db=config["DB"])

class Producto():
    def get_productos(self):
        conexion = getConexion()
        productos = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
        conexion.close()
        return productos
    
    def get_by_id(self, id: int)-> tuple:
        try:
            conexion = getConexion()
            cur = conexion.cursor()
            sql = "SELECT * FROM productos WHERE id = {id}"
            cur.execute(sql.format(id = id))
            data = cur.fetchall()
            conexion.close()
            return data[0]
        except:
            print('Error function det_by_id')


    def delete_producto(self, id):
        conexion = getConexion()
        try:
            with conexion.cursor() as cursor:
                cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
            conexion.commit()
            conexion.close()
        except:
            print("Error 002 function delete_contacto")
    
    def update_producto(self, id: int , nombre: str, imagen: int, precio: str) -> int:
        try:
            conexion = getConexion()
            cur = conexion.cursor()
            sql = 'UPDATE productos SET nombre = %s, imagen = %s, precio = %s WHERE id = %s'
            values = (nombre, imagen, precio, id)
            cur.execute(sql, values)
            conexion.commit()
            conexion.close()
        except:
            print('Error function update_contacto')

    def add_producto(self, nombre, imagen, precio):
        conexion = getConexion()
        cur = conexion.cursor()
        cur.execute('INSERT INTO productos (nombre, precio, imagen) VALUES ( %s, %s, %s)', (nombre, precio, imagen)) 
        conexion.commit()
        conexion.close()


            
#     def update_contacto(self, id: int , nombre: str, telefono: int, email: str) -> int:
#         try:
#             cur = self.mysql.connection.cursor()
#             sql = 'UPDATE contactos SET nombre = %s, telefono = %s, email = %s WHERE id = %s'
#             values = (nombre, telefono, email, id)
#             cur.execute(sql, values)
#             self.mysql.connection.commit()
#             print(cur.rowcount, "record(s) updated")
#             return cur.rowcount
#         except:
#             print('Error function update_contacto')
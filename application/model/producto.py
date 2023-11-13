from application.config import CONFIG
import pymysql

config = CONFIG["DATABASE"]

class Producto():
    def __init__(self):
        self.db = pymysql.connect(host=config["HOST"],
                                user=config["USER"],
                                password=config["PASSWORD"],
                                db=config["DB"])

    def get_productos(self):
        productos = []
        with self.db.cursor() as cursor:
            cursor.execute("SELECT * FROM productos")
            productos = cursor.fetchall()
        # self.db.close()
        return productos

    def delete_contactos(self, id):
        try:
            cur = self.db.connection.cursor()
            sql = "DELETE FROM productos WHERE id = {id}"
            cur.execute(sql.format(id = id))
            self.db.connection.commit()
            print(cur.rowcount, "record(s) deleted")
            return cur.rowcount
        except:
            print("Error 002 function delete_contacto")


#     def add_contacto(self, nombre, telefono, email):
#         try:
#             cur = self.mysql.connection.cursor()
#             cur.execute('INSERT INTO contactos (nombre, telefono, email) VALUES ( %s, %s, %s)', (nombre, telefono, email)) #preparamos la consulta con el metodo execute del metodo con 
#             self.mysql.connection.commit()
#         except:
#             print("Error 001 function add_contacto")

#     def delete_contactos(self, id):
#         try:
#             cur = self.mysql.connection.cursor()
#             sql = "DELETE FROM contactos WHERE id = {id}"
#             cur.execute(sql.format(id = id))
#             self.mysql.connection.commit()
#             print(cur.rowcount, "record(s) deleted")
#             return cur.rowcount
#         except:
#             print("Error 002 function delete_contacto")


#     def get_by_id(self, id: int)-> tuple:
#         try:
#             cur = self.mysql.connection.cursor()
#             sql = "SELECT * FROM contactos WHERE id = {id}"
#             cur.execute(sql.format(id = id))
#             data = cur.fetchall()
#             return data
#         except:
#             print('Error function det_by_id')

            
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

# productos = [
#     {
#         "id": 1,
#         "nombre": "Zapatos Nike",
#         "imagen": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
#         "precio": 80
#     },
#     {
#         "id": 2,
#         "nombre": "Audifonos",
#         "imagen": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
#         "precio": 20
#     },
#     {
#         "id": 3,
#         "nombre": "Reloj",
#         "imagen": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1099&q=80",
#         "precio": 50
#     },
#     {
#         "id": 4,
#         "nombre": "Smartwatch",
#         "imagen": "https://images.unsplash.com/photo-1546868871-7041f2a55e12?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80",
#         "precio": 90
#     },
#     {
#         "id": 5,
#         "nombre": "Perfume",
#         "imagen": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1074&q=80",
#         "precio": 50
#     }
    
# ]
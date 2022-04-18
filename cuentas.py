#importar tkinter
from tkinter import ttk
from tkinter import *


#importar mysql
import mysql.connector


#Clase product
class Usuarios:
    def __init__(self, window):
        self.wind = window
        self.wind.title('MOVISTAR PLAY')
        #Creating a frame container
        frame = LabelFrame(self.wind, text = 'Registrar una nueva cuenta')
        frame.grid(row = 0, column = 0, columnspan = 5, pady = 20)

        #correo input
        Label(frame, text = 'Correo: ').grid(row = 1, column = 0)
        self.email = Entry(frame)
        self.email.focus()
        self.email.grid(row = 1, column = 1)

        #contraseña input
        Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
        self.password = Entry(frame)
        self.password.grid(row = 2, column = 1)

        #boton registrar
        ttk.Button(frame, text = 'Registrar', command = self.add_user).grid(row = 4, columnspan = 2, sticky = W + E)

        #Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 5, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Correo', anchor = CENTER)
        self.tree.heading('#1', text = 'Contraseña', anchor = CENTER)

        self.get_users()
    
    #metodo para conectar a la base de datos
    def run_query(self, query, parameters = ()):
        #conectar a la base de datos
        db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'movplay',
            port = 3306
        )
        #crear el cursor
        cursor = db.cursor()
        #ejecutar la consulta
        cursor.execute(query, parameters)
        #guardar los cambios
        #obtener los resultados
        result = cursor.fetchall()
        #cerrar el cursor
        cursor.close()
        #cerrar la conexion
        db.close()
        #retornar los resultados
        return result

    # Get Products from Database
    def get_users(self):
        #limpiar la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)        
        #ejecutar la consulta
        query1 = 'SELECT id_cuenta, correo, contraseña FROM cuentas'
        #ejecutar la consulta
        db_rows = self.run_query(query1)
        print(query1)
        #recorrer los registros
        for row in db_rows:
            #agregar los registros a la tabla
            self.tree.insert('', 0, text = row[1], values = row[2])

    #Validar input vacío
    def validation(self):
        return len(self.email.get()) != 0 and len(self.password.get()) != 0

    #agregar nueva cuenta
    def add_user(self):
        if self.validation():
            #insertar los datos en la base de datos mysql
            query2 = "INSERT INTO cuentas VALUES (NULL, '{0}','{1}', NULL)".format(self.email.get(), self.password.get())
            print(query2)
            #ejecutar la query
            self.run_query(query2)
        else:
            print('Ingrese todos los datos')
        self.get_users()

if __name__ == '__main__':
    #ejecuta tk
    window = Tk()
    application = Usuarios(window)
    window.mainloop()


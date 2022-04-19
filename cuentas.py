#importar tkinter
from ast import operator
from tkinter import ttk
from tkinter import *
from turtle import position
from colorama import Cursor


#importar mysql
import mysql.connector


#Clase product
class Usuarios:
    def __init__(self, window):
        self.wind = window
        self.wind.title('MOVISTAR PLAY')
        self.wind.geometry('403x500')
       
        # #crear un frame
        # frame_botones = Frame(self.wind, height = 22, bg = 'blue')
        # frame_botones.grid(row = 0, column = 0, columnspan=2, sticky = W + E)

        # #crear 3 botones dentro de frame_botones
        # self.principal = Button(frame_botones, text = 'Principal', height = 1)
        # self.principal.grid(row = 0, column = 0, sticky = W + E)

        # self.usuarios = Button(frame_botones, text = 'Usuarios', height = 1)
        # self.usuarios.grid(row = 0, column = 1, sticky = W + E)

        # self.cuentas = Button(frame_botones, text = 'Cuentas', height = 1)
        # self.cuentas.grid(row = 0, column = 2, sticky = W + E)

        ttk.Button(text='Principal').grid(row=0, column=0,columnspan=2, sticky=W + E)
        ttk.Button(text='Usuarios').grid(row=0, column=2,columnspan=2, sticky=W + E)
        ttk.Button(text='Cuentas').grid(row=0, column=4,columnspan=2, sticky=W + E)


        #Creating a frame container
        frame = LabelFrame(self.wind, text = 'Registrar una nueva cuenta', padx=10, pady=7)
        frame.grid(row = 1, column = 0, columnspan = 6, pady = 20)

        #correo input
        Label(frame, text = 'Correo: ').grid(row = 1, column = 0, padx=10, pady=10)
        self.email = Entry(frame)
        self.email.focus()
        self.email.grid(row = 1, column = 1)

        #contraseña input
        Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
        self.password = Entry(frame)
        self.password.grid(row = 2, column = 1)

        #boton registrar
        ttk.Button(frame, text = 'Registrar', command = self.add_user).grid(row = 4, columnspan = 2, sticky = W + E)

        #message
        self.message = Label(text = '', fg = 'red')
        self.message.grid(row = 3, column = 0, columnspan = 6, sticky = W + E)


        #Table
        self.tree = ttk.Treeview(height = 10, columns = 2,)
        self.tree.grid(row = 5, column = 0, columnspan = 6)
        self.tree.heading('#0', text = 'Correo', anchor = CENTER)
        self.tree.heading('#1', text = 'Contraseña', anchor = CENTER)

        #botones
        ttk.Button(text = 'Eliminar').grid(row = 6, column = 0,columnspan=3, sticky = W + E)
        ttk.Button(text = 'Editar').grid(row = 6, column = 3,columnspan=3, sticky = W + E)

        


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

        #obtener los registros
        if query.lower().startswith('select'):
            #obtener los registros
            records = cursor.fetchall()
            #cerrar el cursor
            cursor.close()
            #desconectar la base de datos
            db.close()
            return records
        else:
            #ejecutar el commit
            db.commit()
            #cerrar el cursor
            cursor.close()
            #desconectar la base de datos
            db.close()
            #mensaje de confirmacion
            print('Registro agregado')

    # Get Products from Database
    def get_users(self):
        #limpiar la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)        
        #ejecutar la consulta
        query = 'SELECT id_cuenta, correo, contraseña FROM cuentas ORDER BY id_cuenta desc'
        #ejecutar la consulta
        db_rows = self.run_query(query)

        #recorrer los registros
        for row in db_rows:
            #agregar los registros a la tabla
            self.tree.insert('', 0, text = row[1], values = row[2])

    #Validar input vacío
    def validation(self):
        return len(self.email.get()) != 0 and len(self.password.get()) != 0

    #agregar nueva cuenta
    def add_user(self):
        #validar que los campos no esten vacios
        if self.validation():
            #ejecutar la consulta
            query = 'INSERT INTO cuentas (correo, contraseña) VALUES (%s, %s)'
            parameters = ( self.email.get(), self.password.get())
            self.run_query(query, parameters)
            self.message['text'] = 'Cuenta agregada'.format(self.email.get())

            #limpiar los campos
            self.email.delete(0, END)
            self.password.delete(0, END)
            self.get_users()
        else:
            #mensaje de error
            self.message['text'] = 'Por favor llene todos los campos'

if __name__ == '__main__':
    #ejecuta tk
    window = Tk()
    application = Usuarios(window)
    window.mainloop()


#importar tkinter
import this
from tkinter import ttk
from tkinter import *

#importar mysql
import pymysql

#Clase product
class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title('MOVISTAR PLAY')
        #Creating a frame container
        frame = LabelFrame(self.wind, text = 'Registrar una nueva cuenta')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        #correo input
        Label(frame, text = 'Correo: ').grid(row = 1, column = 0)
        self.email = Entry(frame)
        self.email.focus()
        self.email.grid(row = 1, column = 1)

        #contraseña input
        Label(frame, text = 'Contraseña: ').grid(row = 2, column = 0)
        self.password = Entry(frame)
        self.password.grid(row = 2, column = 1)

        #usuario input
        Label(frame, text = 'Usuario: ').grid(row = 3, column = 0)
        self.user = Entry(frame)
        self.user.grid(row = 3, column = 1)

        #boton registrar
        ttk.Button(frame, text = 'Registrar').grid(row = 4, columnspan = 2, sticky = W + E)

        #Table
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 5, column = 0, columnspan = 2)
        self.tree.heading('#0', text = 'Name', anchor = CENTER)
        self.tree.heading('#1', text = 'Email', anchor = CENTER)

if __name__ == '__main__':
    #ejecuta tk
    window = Tk()
    application = Product(window)
    window.mainloop()
import sys
from tkinter import *



""" Definición de funciones para la barra de menús """
#-----------------------------------------------------------------------------#
""" Para cerrar la ventana principal """
def mQuit():
    mExit = messagebox.askyesno(title="Cerrar ventana",message="¿Está seguro?")
    if mExit > 0:
        mGui.destroy()
        return


""" Llamar a las funciones (lexico, sintactico) de Tkinter a dll """

def openConsolaTK():
    import Consola
    def main():
        "Ejecutar la consola."

    if __name__ == "__main__":
        main()
    



"""Definición de comandos para la ventana Consola """
def openConsola():
    mGuiConsola=Tk()
    mGuiConsola.config(bg="white")
    mGuiConsola.geometry('250x250+900+100')#tamaño de la ventana principal
    mGuiConsola.title('Consola ~SWI Prolog~')#Nombre de la ventana principal

    
""" Definir la ventana principal """
mGui = Tk() #master
mGui.config(bg="white") #color del fondo de la ventana
mGui.geometry('500x575+400+50')#tamaño de la ventana
mGui.title('~SWI Prolog~')#Nombre de la ventana
mlabel = Label(mGui,text ='SWI Prolog',fg='white', bg='black').pack() #TÍTULO 


""" Ventana con imagen """
fondo=PhotoImage(file="Buho12.gif") # Imagen
fondoLabel=Label(mGui,image=fondo,bd=2,bg="#000000") #Define la imagen como un label#
fondoLabel.image=fondo
fondoLabel.pack()

mlabel = Label(mGui, text='~Consola de Prolog en Python~',fg='white', bg='black').pack() #label inferior#


""" Botones dentro de la ventana principal """
mbuttonConsola = Button(mGui, text='Ir a consola', command = openConsolaTK, fg='black', bg='sky blue').place(x=70, y=20)
mbuttonBaseConocimientos = Button(mGui, text='Base de Conocimientos',command = openConsola, fg='black', bg='sky blue').place(x=320, y=20)


""" Construcción de la barra de menús """
menubar=Menu(mGui)#Barra de menú

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label = "Exit",command = mQuit)
menubar.add_cascade(label = "File",menu=filemenu)

mGui.config(menu=menubar)



mGui.mainloop() #para que funcione en Windows

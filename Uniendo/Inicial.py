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


##""" Llamar a las funciones (lexico, sintactico) de Tkinter a dll """
##
##def llamarFunciones():
##    from jugar import main
##    from director import Director
##    from escenas import EscenaTitulo
##    def main():
##        "Ejecutar el juego."
##        director = Director("**Snake**")
##        director.ejecutar(EscenaTitulo(), 10)
##    if __name__ == "__main__":
##        main()
##    
##
    
""" Definir la ventana principal """
mGui = Tk() #master
mGui.config(bg="white") #color del fondo de la ventana
mGui.geometry('500x500+455+100')#tamaño de la ventana
mGui.title('~SWI Prolog~')#Nombre de la ventana
mlabel = Label(mGui,text ='SWI Prolog',fg='red', bg='green').pack() #TÍTULO 

fondo=PhotoImage(file="Buho12.gif")
fondoLabel=Label(mGui,image=fondo,bd=2,bg="#000000")
fondoLabel.image=fondo
fondoLabel.pack()



""" Construcción de la barra de menús """
menubar=Menu(mGui)#Barra de menú

filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label = "Exit",command = mQuit)
menubar.add_cascade(label = "File",menu=filemenu)

mGui.config(menu=menubar)



mGui.mainloop() #para que funcione en Windows

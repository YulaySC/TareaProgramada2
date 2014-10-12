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
mGui.title('Juego ~SWI Prolog~')#Nombre de la ventana
mlabel = Label(mGui,text ='SNAKE',fg='red', bg='black').pack() #TÍTULO 

##fondo=PhotoImage(file="buho.gif")
##fondoLabel=Label(mGui,image=fondo,bd=2,bg="#000000")
##fondoLabel.image=fondo
##fondoLabel.pack()
##
##""" definir modos de juego """ ##""" Botones """##
##
##""" Botón de Modo Juego """
##mbuttonModoJuego = Button(mGui,text='Modo juego',fg = 'white', bg = 'blue').place(x=70,y=20)
##
##tamaño = Label(mGui,text ='Dimensiones de la ventana deseada:',fg='white',bg='green').place(x=20,y=50)
##recuerde = Label(mGui,text ='Recuerde:',fg='white',bg='green').place(x=70,y=70)
##Largo = Label(mGui,text='Largo: 15 -- 50',fg='white',bg='green').place(x=70,y=90)
##Ancho = Label(mGui,text='Ancho: 15 -- 25',fg='white',bg='green').place(x=70,y=110)
##
##Medida1=Entry(mGui)
##Medida1.place(x=50,y=130)
##
##Medida2=Entry(mGui)
##Medida2.place(x=50,y=150)
##mbuttonOK = Button(mGui,text='OK',command= validar, fg = 'white', bg = 'blue').place(x=50,y=170)
##
##
##
##""" Construcción de la barra de menús """
##menubar=Menu(mGui)#Barra de menú
##
##filemenu = Menu(menubar,tearoff=0)
##filemenu.add_command(label = "Exit",command = mQuit)
##menubar.add_cascade(label = "File",menu=filemenu)
##
##mGui.config(menu=menubar)
##
##WIDTH=Medida1.get()
##HEIGHT=Medida2.get()

mGui.mainloop()

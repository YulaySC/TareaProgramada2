# -*- coding: cp1252 -*-

import sys
from tkinter import *

from pprint import pprint
from datetime import *

import datetime
import shutil
import glob
import time
import sys
import os



""" Definicion de la ventana principal root """
root = Tk()
root.config(bg="black")
root.title("Consola de SWI Prolog en Python")
root.geometry("610x435+300+100")



menu_general = LabelFrame(root, background = "#2E2E2E") # el LabelFrame es necesario como base para apoyar los menus sobre el
menu_general.pack(side = TOP)

time1 = '' 
clock = Label(menu_general, font=('ubuntu', 10, 'bold'), bg='#3C3B37',fg='white', bd=0) 
clock.pack(side = RIGHT)

def tick(): 
    global time1 
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1: 
        time1 = time2 
        clock.config(text=time2,background = "#585858") 
    clock.after(200, tick)

"""
boton_menu_archivo = Menubutton(menu_general, text = "Color de la fuente", foreground = "white", background = "#585858",
                                activebackground = "#424242", activeforeground = "#585858")  #creamos el boton del menu del cual despus desplegamos los menus
boton_menu_archivo.pack(side = LEFT) #ahora si es verdaderamente visible

menu_archivo = Menu(boton_menu_archivo, background = "#424242", foreground = "#23A3FF",
                    activebackground = "#474AFF", activeforeground = "#70DBFF")
menu_archivo.add_command(label = "Color de fuente Azul", compound = LEFT, command = bluecollor)
menu_archivo.add_command(label = "Color de fuente Rojo", compound = LEFT, command = redcolor)
menu_archivo.add_command(label = "Color de fuente Blanco", compound = LEFT, command = whitecolor)
menu_archivo.add_command(label = "Color de fuente Gris", compound = LEFT, command = griscolor)
menu_archivo.add_command(label = "Color de fuente naranja", compound = LEFT, command = narancolor)
menu_archivo.add_command(label = "Color de fuente Amarillo", compound = LEFT, command = amancolor)
menu_archivo.add_command(label = "Color de fondo  Verde", compound = LEFT, command = aman2color)
menu_archivo.add_command(label = "Color de fondo  Negro", compound = LEFT, command = bcolor)
menu_archivo.add_separator()
menu_archivo.add_command(label = "Exit", compound = LEFT, command = root.destroy)

boton_menu_archivo["menu"] = menu_archivo
"""


"""

boton_menu_archivo2 = Menubutton(menu_general, text = "Color de Fondo", foreground = "white", background = "#585858",
                                activebackground = "#424242", activeforeground = "#585858")  #creamos el boton del menu del cual despus desplegamos los menus
boton_menu_archivo2.pack(side = LEFT) #ahora si es verdaderamente visible

menu_archivo2 = Menu(boton_menu_archivo2, background = "#424242", foreground = "#23A3FF",
                    activebackground = "#474AFF", activeforeground = "#70DBFF")
menu_archivo2.add_command(label = "Color de fondo Azul", compound = LEFT, command = bluecollor2)
menu_archivo2.add_command(label = "Color de fondo  Rojo", compound = LEFT, command = redcolor2)
menu_archivo2.add_command(label = "Color de fondo  Blanco", compound = LEFT, command = whitecolor2)
menu_archivo2.add_command(label = "Color de fondo  Gris", compound = LEFT, command = griscolor2)
menu_archivo2.add_command(label = "Color de fondo  naranja", compound = LEFT, command = narancolor2)
menu_archivo2.add_command(label = "Color de fondo  Amarillo", compound = LEFT, command = amancolor2)
menu_archivo2.add_command(label = "Color de fondo  Verde", compound = LEFT, command = aman2color2)
menu_archivo2.add_command(label = "Color de fondo  Negro", compound = LEFT, command = bcolor2)
menu_archivo2.add_separator()
menu_archivo2.add_command(label = "Exit", compound = LEFT, command = root.destroy)

boton_menu_archivo2["menu"] = menu_archivo2

"""




 
def colocar_scrollbar(listbox,scrollbar):
    scrollbar.config(command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox.pack(side=LEFT, fill=Y)


 
frame1=Frame(root,bg="red")
#frame1.place(x=200, y=100) # <-> -|^ x= -> y= -|^
frame1.pack()
scroll1=Scrollbar(frame1)
list1=Listbox(frame1,bg="black",fg='green',width=80,height=20,font=("Helvetica", 10))
list1.pack()
colocar_scrollbar(list1,scroll1)
mivalor=StringVar()
copi2=StringVar()
copi3=StringVar()

#Label(root,image=imagen1).pack()

e1=Entry(root,textvar=mivalor,width=60,bg="black",fg="green", font=("Helvetica", 10)).place(x=10, y=380) # <-> -|^ x= -> y= -|^

"""
labels dentro de la consola pequeña
"""
list1.insert(END, "Consola de Prolog en Python")
list1.insert(END, ">>")


#-----------------------------------------------------------------------------------------#
## -- Define cómo interpretar lo de la caja -- ##
def insertar_en_listbox():

    if mivalor.get() != '':
        
        if mivalor.get() == "help":
            
            list1.insert(END,'')
            list1.insert(END,'HELP:            Muestra la lista de comandos de la shell')
            list1.insert(END,"-H:              Muestar la lista de los comandos de la shell")
            list1.insert(END,'DEL:             Elimina el archivo marcado')
            list1.insert(END,'XDEL:            Elimina la carpeta marcada')
            list1.insert(END,'CLS                Borra la pantalla')
            list1.insert(END,'TIME:            Muestra la hora y fecha del sistema')
            list1.insert(END,'PRINT:           Muestra mensajes en la pantalla')
            list1.insert(END,'READ:            Abre el archivo en modo escritura')
            list1.insert(END,'WANT:            Buasca un todos los archivo con extension a elegir')
            list1.insert(END,'DIR:             Muestra el directorio actual')
            list1.insert(END,'CD:              Cambia de directorio al directorio selecionado')
            list1.insert(END,'LAST:            Muestra la fecha de la ultima midificacion del un archivo marcado')
            list1.insert(END,'EXIT:            Sale de la consola de comandos')

            list1.insert(END, "")
            #list1.insert(">>")

        if mivalor.get() == "-h":
            list1.insert(END,'')
            list1.insert(END,'HELP:            Muestra la lista de comandos de la shell')
            list1.insert(END,"-H:              Muestar la lista de los comandos de la shell")
            list1.insert(END,'DEL:             Elimina el archivo marcado')
            list1.insert(END,'XDEL:            Elimina la carpeta marcada')
            list1.insert(END,'CLS                Borra la pantalla')
            list1.insert(END,'TIME:            Muestra la hora y la fecha del sistema')
            list1.insert(END,'PRINT:           Muestra mensajes en la pantalla')
            list1.insert(END,'READ:            Abre el archivo en modo escritura')
            list1.insert(END,'WANT:            Buasca un todos los archivo con extension a elegir')
            list1.insert(END,'DIR:             Muestra el directorio actual')
            list1.insert(END,'CD:              Cambia de directorio al directorio selecionado')
            list1.insert(END,'LAST:            Muestra la fecha de la ultima midificacion del un archivo marcado')
            list1.insert(END,'EXIT:            Sale de la consola de comandos')
            list1.insert(END, "")
            #list1.insert(END, ">>")

        if mivalor.get() == "HELP":
            
            list1.insert(END,'')
            list1.insert(END,'HELP:            Muestra la lista de comandos de la shell')
            list1.insert(END,"-H:              Muestar la lista de los comandos de la shell")
            list1.insert(END,'DEL:             Elimina el archivo marcado')
            list1.insert(END,'XDEL:            Elimina la carpeta marcada')
            list1.insert(END,'CLS                Borra la pantalla')
            list1.insert(END,'TIME:            Muestra la hora y la fecha del sistema')
            list1.insert(END,'PRINT:           Muestra mensajes en la pantalla')
            list1.insert(END,'READ:            Abre el archivo en modo escritura')
            list1.insert(END,'WANT:            Buasca un todos los archivo con extension a elegir')
            list1.insert(END,'DIR:             Muestra el directorio actual')
            list1.insert(END,'CD:              Cambia de directorio al directorio selecionado')
            list1.insert(END,'LAST:            Muestra la fecha de la ultima midificacion del un archivo marcado')
            list1.insert(END,'EXIT:            Sale de la consola de comandos')
            list1.insert(END, "")
            list1.insert(END, ">>")

        if mivalor.get() == "-H":
            list1.insert(END,'')
            list1.insert(END,'HELP:            Muestra la lista de comandos de la shell')
            list1.insert(END,"-H:              Muestar la lista de los comandos de la shell")
            list1.insert(END,'DEL:             Elimina el archivo marcado')
            list1.insert(END,'XDEL:            Elimina la carpeta marcada')
            list1.insert(END,'CLS                Borra la pantalla')
            list1.insert(END,'TIME:            Muestra la hora y fecha del sistema')
            list1.insert(END,'PRINT:           Muestra mensajes en la pantalla')
            list1.insert(END,'READ:            Abre el archivo en modo escritura')
            list1.insert(END,'WANT:            Buasca un todos los archivo con extension a elegir')
            list1.insert(END,'DIR:             Muestra el directorio actual')
            list1.insert(END,'CD:              Cambia de directorio al directorio selecionado')
            list1.insert(END,'LAST:            Muestra la fecha de la ultima midificacion del un archivo marcado')
            list1.insert(END,'TIME             Muestra la hora del sistema')
            list1.insert(END,'EXIT:            Sale de la consola de comandos')
            list1.insert(END, "")
            #list1.insert(END, ">>")

        if mivalor.get().startswith("del") == True:

            rut = mivalor.get()[4:]

            try:
                os.remove(rut)
                list1.insert(END,'EL archivo a sido eliminado con exito.')

            except:
                list1.insert(END,'ERROR El archivo no a podido ser eliminado.')

            list1.insert(END, "")
            list1.insert(END, ">>")

        if mivalor.get().startswith("xdel") == True:

            arc1 = mivalor.get()[5:]
            boo = True

            try:
                shutil.rmtree(arc1, boo)
                list1.insert(END, "\nLa carpeta a sido eliminada.")

            except:
                list1.insert(END,"ERROR La carpeta no a podido ser eliminado.")

            list1.insert(END, "")
            list1.insert(END, ">>")
                
        if mivalor.get().startswith("read") == True:

            red = mivalor.get()[5:]

            try:
                archi = open(red,'r')
                linea=archi.readline()
                while linea!="":
                    list1.insert(END,linea)
                    linea=archi.readline()

            except:
                list1.insert(END,"ERROR El archivo no a podido ser abierto en mode lectura.")

            list1.insert(END, "")
            list1.insert(END, ">>")

        elif mivalor.get().startswith("want") == True:

            arc = mivalor.get()[5:]

            try:

                lista = glob.glob("*" + arc)
                list1.insert(END,"Archivos con extension" + arc + "en este directorio:")
                list1.insert(END,"")
                list1.insert(END,lista)
                
            except:
                list1.insert(END,"ERROR No se a encontrado el archivo con la extension que pide.")

            list1.insert(END, "")
            list1.insert(END,">>")


        elif mivalor.get().startswith(">>") == True:

            arc = mivalor.get()[4:]
            try:
                os.chdir(arc)
                list1.insert(END,"")
                list1.insert(END,">>:")
                list1.insert(END,"")

                archis = os.listdir(arc)
                for imagen in archis:
                    list1.insert(END,imagen)

            except:
                
                list1.insert(END,"")
                list1.insert(END,">>:")
                list1.insert(END,"")
                

                archis = os.listdir(os.getcwd())
                for imagen in archis:
                    list1.insert(END,imagen)

            list1.insert(END, "")
            list1.insert(END, ">>")
                    
        elif mivalor.get().startswith(">>") == True:

            arc = mivalor.get()[3:]
            try:
                os.chdir(arc)
            except:
                list1.insert(END,os.getcwd())
                
            list1.insert(END, "")
            list1.insert(END, ">>")

        elif mivalor.get().startswith("last") == True:

            arcx = mivalor.get()[5:]

            try:
                metadata = os.stat(arcx)
                metadata.st_mtime
                time.localtime(metadata.st_mtime)

                list1.insert(END,"")
                list1.insert(END,time.localtime(metadata.st_mtime))
                list1.insert(END,"")

            except:
                list1.insert(END,"ERROR Archivo no definido.")

            list1.insert(END, "")
            list1.insert(END, ">>")

        elif mivalor.get().startswith("print") == True:

            rut = mivalor.get()[6:]

            list1.insert(END,rut)
            
            list1.insert(END, "")
            list1.insert(END, ">>")

        elif mivalor.get() == 'time':

            list1.insert(END, '')

            list1.insert(END, datetime.datetime.now())

            list1.insert(END, "")
            list1.insert(END, ">>")

        elif mivalor.get() == 'cls':
            list1.delete(0, END)           
            
            

        elif mivalor.get() == "exit":
            exit()

                



    elif mivalor.get() == '':
        list1.insert(END,"No se reconoce como un comando interno o externo")

#-----------------------------------------------------------------------------------------# 
        

b1=Button(root,text="Enter",command=insertar_en_listbox, bg="black",fg="green", width=20).place(x=450, y=380) # <-> -|^ x= -> y= -|^
# b2=Button(root,text="Copiar",command=copyfuncion, bg="black",fg="green", width=20).place(x=1100, y=700) # <-> -|^ x= -> y= -|^

tick()
clock.mainloop()

root.mainloop()

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

##
import versionV2

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

###############################
import ply.lex as lex 

# List of token names.   This is always required
tokens = [
 # Literals (identifier, integer constant, float constant, string constant, char const)
    'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST','NAME',#'NUM'

    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    
    # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Structure dereference (->)
    'ARROW',

    # Ternary operator (?)
    'TERNARY',
    
    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Ellipsis (...)
    'ELLIPSIS',

    'FLOAT','INTEGER','CHARACTER','STRING','INCREMENT','DECREMENT','MODULO'
]
    
# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'%'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LSHIFT           = r'<<'
t_RSHIFT           = r'>>'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

# Assignment operators

t_EQUALS           = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='
t_LSHIFTEQUAL      = r'<<='
t_RSHIFTEQUAL      = r'>>='
t_ANDEQUAL         = r'&='
t_OREQUAL          = r'\|='
t_XOREQUAL         = r'^='

# Increment/decrement
t_INCREMENT        = r'\+\+'
t_DECREMENT        = r'--'

# ->
t_ARROW            = r'->'

# ?
t_TERNARY          = r'\?'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_PERIOD           = r'\.'
t_SEMI             = r';'
t_COLON            = r':'
t_ELLIPSIS         = r'\.\.\.'

# Identifiers
t_ID = r'[A-Z][A-Za-z0-9_]*'
t_NAME    = r'[a-z][a-zA-Z0-9_]*'
#t_NUM=r'[0-9]*'

# Integer literal
t_INTEGER = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FLOAT = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_STRING = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comment (C-Style)
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t

# Comment (C++-Style)
def t_CPPCOMMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t.type

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t
#def t_NEWLINE(t):
#    r'\n'
#    t.lexer.lineno += 1
#    return t
#def t_ID(t):
#    r'[A-Z][A-Z0-9]*'
#    if t.value in keywords:
#        t.type = t.value
#    return t
    


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print ("Illegal character '%s' " % t.value[0])
    t.lexer.skip(1)

# Build the lexer

#print('PRUEBA------ DIGITE LO QUE DESEE:')
#data=input()
#lexer.input(data)

# Tokenize
def lexicalTYPE (data):
    lexer = lex.lex()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        #tok.line
        return (tok.type)
           
        for tok in lexer:
            return (tok.type)
def RetlexicalTYPE(data):
    lexer = lex.lex()
    lexer.input(data)
    elem=[]
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        #tok.line
        elem.append(tok.type)
        #return (elem)
           
        for tok in lexer:
            elem.append(tok.type)
    return (elem)

def PARENT(data):
    elementos=RetlexicalTYPE(data)
    cont=len(elementos)-1
    contador=len(elementos)-1
    
    print (cont)
    print(contador)
    existe=False
    while(cont>=0):
        if((elementos[cont])=='LPAREN'):
            if((elementos[contador-1])=='RPAREN'):
                existe=True
                return (existe)
        cont=cont-1

    return (existe)
            

def arg(data):
    lexer = lex.lex()
    lexer.input(data)
    elem=[]
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        #tok.line
        elem.append(tok.type)
        return (elem)
           
        for tok in lexer:
            elemn.append(tok.type)
            return (elemn)
        
def lexicalVALUE (data):
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok: break      # No more input
        return(tok.value)
           
        for tok in lexer:
            return(tok.value)

def sintaxis():
 print ('Welcome to SWI-Prolog (Multi-threaded, 32 bits, Version 6.6.4 n/Copyright (c) 1990-2013 University of Amsterdam, VU Amsterdam n/SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software, n/and you are welcome to redistribute it under certain conditions. n/Please visit http://www.swi-prolog.org for details. n/For help, use ?- help(Topic). or ?- apropos(Word).')
 val1=input()
 datos=[]
 lexer = lex.lex()
 elementos=[]
 y=False
 boolean= False
 if (val1=='<define>'):
     
     while(y==False):
    #print('entro')
         print ('>>')
         val1=input()
         data=val1
         cont=0
         elementos=RetlexicalTYPE(data)
         contlistelem=len(elementos)-1
         if (elementos[0]=='NAME'):
             if(elementos[contlistelem]=='PERIOD'):
                 if (val1!='</define>.'):
                     datos.append(val1)
        #print(datos[cont])
                     cont=cont+1
                     print ('>>')
                     val1=input()
    #print ('salio')
         if (val1=='</define>.'):
             y=True
         else:
             print ('Valor invalido')
             print ('>>')
             val1=input()
        
 if(val1=='</define>.'):
     print('?')
     val2=input()
     int=0
     x=False
     while(x==False):
         for i in range(0,len(datos)):
             cont=cont-1
             if(val2==datos[cont]):
                 boolean=True
             cont=cont-1
         x=True
     if(boolean==True):
         print('Yes')
     else:
         print('No')
       
        #print ('salio')
 else:
     print('error')

#class Aridad:
#    cont=0;
#    val=""
#    const=""
#    def contador(self,dato):
#        if 
    

            
###############################


 
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
        """
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
            """
        """
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
        """

             
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


        elif mivalor.get() == "inicio":
            #from versionV2 import sintaxis
            #if mivalor.get() == "sintaxis":
            list1.insert(END, "funca")
            return sintaxis()

         
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

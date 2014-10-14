
def sintaxis():
 print ('Welcome to SWI-Prolog (Multi-threaded, 32 bits, Version 6.6.4 n/Copyright (c) 1990-2013 University of Amsterdam, VU Amsterdam n/SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software, n/and you are welcome to redistribute it under certain conditions. n/Please visit http://www.swi-prolog.org for details. n/For help, use ?- help(Topic). or ?- apropos(Word).')
 val1=input()
 datos=[]
 if (val1=='<define>'):
     while(val1=='<define>'):
         print('entro')
         print ('>>')
         val1=input()
         cont=0
         boolean= False
         while (val1!='</define>.'):
             datos.append(val1)
        #print(datos[cont])
             cont=cont+1
             print ('>>')
             val1=input()
             print ('salio')
             if (val1=='</define>.'):
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
        
        #for i in range(0,(datos)):
         #   while(int<=cont):
          #      revisar=datos[int]
           #     if(revisar==val2):
            #        boolean= True
             #   int=int+1
         if(boolean==True):
             print('Yes')

         else:
             print('No')
        
        #print ('salio')
 else:
     print('error')
 



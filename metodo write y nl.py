def inicio(): #Modo consulta (Inicio de programa)
    global ListaRes
    global l_vars
    estado = 1
    while estado:
        string = input("?- ")
        val = inicio_verificaciones(string)
        if string == '':
            pass
        elif string == "<define>":
            consulta()
        elif string == "Exit":
            estado = 0
        elif string == "nl":
            print()
        elif string == "i_BC":
            print(BC)
        elif val[0:5] == "Error":
            print(val)
        else:
            string = fragmenta(string)
            if string[0] == "write":
                escribe(string[1])
            else:
                new_str = hecho(string[0],string[1])
                l_vars = {}
                if comp_hecho_predicado(new_str) == True:
                    print("YES")
                else:
                    print("NO")
    print("Finalizaste")

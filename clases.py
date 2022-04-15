class Usuario:
    op=1
    while op != 5:
        print("1 Crear un usuario")
        print("2 Modificar usuario")
        print("3 Eliminar usuario")
        print("4 Listar usuarios ")
        print("5 Salir")
        op = int(input("Ingrese una opcion:  "))
        print("--------------------------------------------------------------------------")
        
        if op == 1:
            nombre = input("ingrese un nombre ")
            apellido = input("ingrese un apellido ")
            edad = input("ingrese una edad ")
            email = input("ingrese un email ")
            print("--------------------------------------------------------------------------")
        elif op == 2:   
            ap=1
   
            print("1 modificar nombre ")
            print("2 modificar apellido ")
            print("3 modificar edad")
            print("4 modificar email ")
            ap = int(input("Ingrese una opcion:  "))

            if ap == 1:
                nombre = input("Modificar nombre: ")
            if ap == 2:
                apellido = input("Modificar apellido: ")
            if ap == 3:
                edad = input("Modificar edad: ")
            if ap == 4:
                email = input("Modificar email: ")
            else:
                print("Ingrese una opcion correcta")        

            print("--------------------------------------------------------------------------")

        elif op == 3:
            ep=1
            print("1 Eliminar nombre ")
            print("2 Eliminar apellido ")
            print("3 Eliminar edad")
            print("4 Eliminar email ")
            ep = int(input("Ingrese una opcion:  "))

            if ep == 1:
                print("Eliminar nombre")
                nombre=" "
            if ep == 2:
                print("Eliminar apellido")
                nombre=" "
            if ep == 3:
                print("Eliminar edad")
                nombre=" "
            if ep == 4:
                print("Eliminar email")
                nombre=" "
            print("--------------------------------------------------------------------------")    
        elif op == 4:
            print("su nombre es "+nombre)
            print("su apellido es "+apellido)
            print("su nombre es "+edad)
            print("su nombre es "+email)
            print("--------------------------------------------------------------------------")
        elif op == 5:
            print ("Salio del programa")
            print("--------------------------------------------------------------------------")
        else:
            print("Ingrese una opcion valida")
        

       



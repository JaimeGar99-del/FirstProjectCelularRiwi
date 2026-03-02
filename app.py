#creacion de nueva factura
while True:
    try:
#apertura de la factura
        nuevafactura = input("Desea realizar una factura? si / no: ").lower()

        if nuevafactura == "si":

            print("--------------------")
            print("|Nombre del cliente|")
            print("--------------------")

            # VALIDACIÓN NOMBRE (solo letras y espacios)
            while True:
                client_name = input("Ingresar nombre del cliente: ").strip()
                if client_name.replace(" ", "").isalpha() and client_name != "":
                    break
                else:
                    print("Nombre no válido. no has escrito algo valido solo se permiten letras.")
#cierre de la factura:                    
        elif nuevafactura == "no":
            print("--------------------")
            print("|Muchas gracias, nos vemos la proxima|")
            print("--------------------")
            break

        else:
            print("Valor no permitido, por favor ingresa si / no.")

    except ValueError:
        print("Error: debes ingresar un número válido.")
    
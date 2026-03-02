def pedir_nombre(mensaje):
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:
                raise ValueError("el nombre no puede estar vacio")
            if any(char.isdigit()for char in valor):
                raise ValueError("EL nombre no puede contener números")
            return valor
        except ValueError as e:
            print(f"Error: {e} intenta de nuevo")



print("=========== CAJA REGISTRADORA ===========")

# Nombre del cliente
while True:
    nombre = input("Nombre del cliente: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
    elif nombre.isnumeric():
        print("El nombre no puede ser solo números.")
    else:
        break
while True:
                membresia = input("Tiene membresia vip si / no: ").lower()
                if membresia == "si":
                    porcentajedescuento = 0.10
                    break
                elif membresia == "no":
                    porcentajedescuento = 0
                    break
                else:
                    print("Valor no permitido, por favor ingresa si / no.")

iva = 0.19
subtotal = 0
contador = 0



# Bucle principal con match case
while True:

    print("\n1. Agregar producto")
    print("2. Terminar compra")

    opcion = input("Seleccione una opción: ").lower()

    match opcion:

        case "1"| "agregar producto"|"agregar":
            contador += 1
            print(f"\n--- Producto # {contador} ---")


            nombre_producto = pedir_nombre("Nombre del prodcuto: ")
                    
        
            # Validar precio
            while True:
                try:
                    precio = float(input("Precio del producto: "))
                    if precio < 0:
                        print("El precio no puede ser negativo.")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número válido.")

            # Validar cantidad
            while True:
                try:
                    cantidad = int(input("Cantidad del producto: "))
                    if cantidad <= 0:
                        print("La cantidad debe ser mayor que 0.")
                    else:
                        break
                except ValueError:
                    print("Ingrese un número entero válido.")
            

            subtotal_producto = precio * cantidad
            subtotal += subtotal_producto

            print("Producto agregado correctamente.")

        case "2":
            break

        case _:
            print("Opción inválida.")


# Cálculos finales
iva_valor = subtotal * iva
descuento = (subtotal + iva_valor)*porcentajedescuento
total = subtotal - descuento

# Factura final
print("\n============= FACTURA =============")
print("Cliente:", nombre)
print("Su producto", nombre_producto)
print("Cantidad de productos:", contador)
print("IVA (19%):", iva_valor)
print("Subtotal:", subtotal)
print("Descuento", descuento)
print("Total", total)

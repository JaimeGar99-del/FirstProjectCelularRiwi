class Producto:
    def __init__(self, nombre, precio): 
        self.nombre = nombre
        self.precio = precio

    def mostrar(self, codigo):
        print(f"{codigo}. {self.nombre} - ${self.precio}")


# Crear productos
p1 = Producto("Camiseta Oversize Negra", 45000)
p2 = Producto("Jean Slim Fit Azul", 85000)
p3 = Producto("Hoodie Street Negro", 75000)


def mostrar_catalogo():
    print("\n===== CATÁLOGO =====")
    p1.mostrar(1)
    p2.mostrar(2)
    p3.mostrar(3)
    print("0. Finalizar compra")
    print("=====================")


total = 0
productos_seleccionados = []

while True:
    mostrar_catalogo()
    opcion = input("Seleccione producto: ")

    if opcion == "1":
        total += p1.precio
        productos_seleccionados.append(p1)
        print(f"Agregaste {p1.nombre}")
    elif opcion == "2":
        total += p2.precio
        productos_seleccionados.append(p2)
        print(f"Agregaste {p2.nombre}")
    elif opcion == "3":
        total += p3.precio
        productos_seleccionados.append(p3)
        print(f"Agregaste {p3.nombre}")
    elif opcion == "0":
        break
    else:
        print("Opción inválida")

print("\n===== RESUMEN DE COMPRA =====")

if productos_seleccionados:
    for producto in productos_seleccionados:
        print(f"- {producto.nombre} - ${producto.precio}")
else:
    print("No seleccionaste productos.")

print(f"\nTotal a pagar: ${total}")
print("Gracias por tu compra 🛍️")
print("----------------------------------------------------------")
print("        RiwiTechStore - Registro De Ventas                ")
print("----------------------------------------------------------")

client_name = input("Ingrese el nombre del cliente: ")
unit_price = float(input("Ingrese precio unitario: "))
quantity_product= int(input("Ingrese cantidad de productos vendidos: "))
vip = input("¿Es miembro VIP? (si/no): ").lower() == "si"

subtotal = unit_price * quantity_product
if vip: 
    discount = subtotal *0.10
else:
    discount = 0

Total = subtotal - discount



print("\n-------- RESUMEN DE VENTA ---------")
print(f"Cliente: {client_name}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: ${discount:.2f}")
print(f"Total final a pagar: ${Total:.2f}")

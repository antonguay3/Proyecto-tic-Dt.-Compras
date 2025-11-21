import pandas as pd
import compras as cm
import unicodedata

pinf=pd.read_csv("productos_informatica.csv")
comp=pd.read_csv("compras.csv")

yes=["si","s","yes","y","ye"]
no=["no","non","n"]



def norinput(inp): #Input sin tildes ni mayus
    return "".join(c for c in unicodedata.normalize("NFD", input(inp)) if unicodedata.category(c) != "Mn").lower()

while True:
    match input("Que función quiere realizar? Utilize los números 1-4.\n1. Hacer un pedido.\n2. Actualizar el precio de compra de un producto.\n3. Consultar los pedidos de un producto.\n4. Consultar los pedidos en un mes.\n"):
        case "1":
            while True:
                try:
                    id_producto=int(input("Introduzca el ID del producto.\n"))
                    if 0<id_producto<len(pinf.index):
                        break
                    else:
                        print("ID inválido")
                except:
                    print("Entráda inválida.")

            while True:
                try:
                    cantidad=abs(int(input("Introduzca la cantidad a pedir.\n")))
                    break
                except:
                    print("Cantidad inválida")

            while True:
                match norinput(f"pedir {cantidad}u de'{pinf.loc[pinf["ID"]==id_producto]["Nombre del producto"].to_string(index=False)}'?\tY/N: "):
                    case x if x in yes:
                        cm.hacer_pedido(id_producto,cantidad)
                        break
                    case x if x in no:
                        break
                    case _:
                        print("Entrada inválida")
                        
        case "2":
            while True:
                try:
                    id_producto=int(input("Introduzca el ID del producto.\n"))
                    if 0<id_producto<len(pinf.index):
                        break
                    else:
                        print("ID inválido")
                except:
                    print("Entráda inválida.")

            while True:
                try:
                    nuevo_precio=abs(float(input("Introduzca el nuevo precio de compra.\n")))
                    break
                except:
                    print("Precio inválido")

            while True:
                match norinput(f"Actualizar precio de compra de'{pinf.loc[pinf["ID"]==id_producto]["Nombre del producto"].to_string(index=False)}' a {nuevo_precio}?\tY/N: "):
                    case x if x in yes:
                        cm.actualizar_precio_compra(id_producto,nuevo_precio)
                        break
                    case x if x in no:
                        break
                    case _:
                        print("Entrada inválida")
                        
        case "3":
            while True:
                try:
                    id_producto=int(input("Introduzca el ID del producto.\n"))
                    if 0<id_producto<len(pinf.index):
                        cm.pedidos_prod(id_producto)
                        break
                    else:
                        print("ID inválido")
                except:
                    print("Entráda inválida.")
                    
        case "4":
            while True:
                try:
                    mes=int(input("Introduzca el mes como número (1-12)\n"))
                    if 0<mes<13:
                        cm.pedido_mes(mes)
                        break
                    else:
                        print("Mes inválido")
                except:
                    print("Entrada inválida")

import pandas as pd

from datetime import datetime

pinf=pd.read_csv("productos_informatica.csv")
comp=pd.read_csv("compras.csv")

coste=0

yes="Yes" or "yes" or "Y" or "y" or "Sí" or "Si" or "sí" or "si" or "S" or "s"

def hacer_pedido(id_producto,cantidad):
    coste=(pinf.loc[pinf["ID"]==id_producto]["Lote"])*(pinf.loc[pinf["ID"]==id_producto]["Precio de compra"])*cantidad
def actualizar_precio_compra(id_producto,nuevo_precio):
    pass
def pedidos_prod(id_producto):
    pass
def pedido_mes(mes):
    pass

def main():
    inp=""
    while True:
        print("Que función quiere realizar? Utilize los números 1-4.\n1. Hacer un pedido.\n2. Actualizar el precio de compra de un producto.\n3. Consultar los pedidos de un producto.\n4. Consultar los pedidos en un mes.")
        inp=input()
        try:
            if 1<=int(inp)<=4:
                inp=(int(inp))
                if inp==1:
                    while True:
                        print("Introduzca el id del producto.\n")
                        inp=input()
                        try:
                            if 0<int(inp)<999: #<---[-]Hay que obtener el máximo id disponible!
                                inp=int(inp)
                                id_producto=inp
                                break
                            else:
                                print("Id inválido\n")
                        except:
                            print("Id inválido\n")
                    while True:
                        print("Introduzca la cantidad a pedir.\n")
                        inp=input()
                        try:
                            if 0<int(inp)<999: #<---[-]Hay que obtener el máximo id disponible!
                                inp=int(inp)
                                cantidad=inp
                                break
                            else:
                                print("Cantidad inválida\n")
                        except:
                            print("Cantidad inválida\n")
                    if input(f"pedir {cantidad} de [id:{id_producto}]? Y/N: ") = yes:
                        pass
                    elif no = no:
                        pass
                    #################################################################
                if inp==2:
                    pass
                if inp==3:
                    pass
                if inp==4:
                    pass
            else:
                print("No existe esa función\n")
        except:
            print("No existe esa función\n")
            

main()
    
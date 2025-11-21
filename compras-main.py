import pandas as pd
import compras as cm

pinf=pd.read_csv("productos_informatica.csv")
comp=pd.read_csv("compras.csv")

yes=["Yes","yes","Y","y","Sí","Si","sí","si","S","s"]
no=["No","no","N","n"]


inp=""

while True: #Bucle con try-except para preguntar que función función quiere realizar#
    print("Que función quiere realizar? Utilize los números 1-4.\n1. Hacer un pedido.\n2. Actualizar el precio de compra de un producto.\n3. Consultar los pedidos de un producto.\n4. Consultar los pedidos en un mes.")
    inp=input()
    try:
        if 1<=int(inp)<=4:
            inp=(int(inp))
            if inp==1:
                
                while True: #Bucle con try-except para preguntar el id del producto a pedir#
                    print("Introduzca el id del producto.\n")
                    id_producto=input()
                    try:
                        if 0<int(id_producto)<len(pinf.index): #<---[-]Hay que obtener el máximo id disponible!
                            id_producto=int(id_producto)
                            break
                        else:
                            print("Id inválido\n")
                    except:
                        print("Entrada inválida\n")
                        
                while True: #Bucle con try-except para preguntar la cantidad a pedir#
                    print("Introduzca la cantidad a pedir.\n")
                    cantidad=input()
                    try:
                        if 0<int(inp): #<---[-]Debería haber un máximo?
                            cantidad=int(cantidad)
                            break
                        else:
                            print("Cantidad inválida\n")
                    except:
                        print("Entrada inválida\n")
                        
                while True: #Bucle con try-except para confirmar el pedido#
                    print(f"pedir {cantidad}u de","'"+pinf.loc[pinf["ID"]==id_producto]["Nombre del producto"].to_string(index=False)+"'"," Y/N: ")
                    inp=str(input())
                    try:
                        if inp in yes:
                            cm.hacer_pedido(id_producto,cantidad)
                            break
                        elif inp in no:
                            break
                        else:
                            print("Respuesta in válida\n")
                    except:
                        print("Entrada inválida\n")
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




    
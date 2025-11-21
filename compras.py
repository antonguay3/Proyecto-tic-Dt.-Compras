import pandas as pd
from datetime import datetime
pinf=pd.read_csv("productos_informatica.csv")
comp=pd.read_csv("compras.csv")
def hacer_pedido(id_producto,cantidad):
    from datetime import datetime
    pinf=pd.read_csv("productos_informatica.csv")
    comp=pd.read_csv("compras.csv")
    fecha=datetime.now()
    coste=(pinf.loc[pinf["ID"]==id_producto]["Lote"])*(pinf.loc[pinf["ID"]==id_producto]["Precio de compra"])*cantidad
    comp.loc[len(comp)]=[fecha.year,fecha.month,fecha.day,id_producto,cantidad,int(coste.iloc[0]),str((pinf.loc[pinf["ID"]==id_producto]["Proveedor"]).iloc[0])]
    comp.to_csv("compras.csv", index=False)
def actualizar_precio_compra(id_producto,nuevo_precio):
    pinf=pd.read_csv("productos_informatica.csv")
    pinf.loc[pinf["ID"]==id_producto,"Precio de compra"]=nuevo_precio
    pinf.to_csv("productos_informatica.csv", index=False)
def pedidos_prod(id_producto):
    comp=pd.read_csv("compras.csv")
    print(comp[comp["ID"]==id_producto])
def pedido_mes(mes):
    comp=pd.read_csv("compras.csv")
    print(comp[comp["Mes"]==mes])
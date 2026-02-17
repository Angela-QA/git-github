lista_productos=[]
def agregar_producto():
    nombre= input("Ingresa el nombre del producto:  ").strip().capitalize()
    precio= int(input("Ingrese el precio del procucto; ").strip())
    lista_productos.append([nombre,precio])
    print(f"Producto '{nombre}, agregado con éxito")

def consultar_producto():
    if lista_productos:
        print(f"|{'Posicion':<6}| {'productos':<14}| {'Precio':<8}|")
        for i,  item in enumerate(lista_productos, start=1):
            print(f"|{i:^7} | {item[0]:^14}|{item[1]:>9}|")
    else:
        print("La lista de productos está vacía- ")
        print("")    

def eliminar_producto():   
        
        if not lista_productos:
            print("La lista de productos está vacía. No hay nada  para borrar. ")
        
        else:
            nombre= input("Ingree el nombre del producto que desea borrar: ").strip().capitalize()
            for item in lista_productos:
                if item[0]== nombre:
                    lista_productos.remove(item)
                    print(f"El producto '{nombre}' eliminado con éxito.\n")
                    break
                else:
                    print(f"El producto '{nombre}' no estexiste en la lista,\n")

def mostrar_menu():
    print("")
    
        
agregar_producto()
consultar_producto()
eliminar_producto()
consultar_producto()
print("hola Git")





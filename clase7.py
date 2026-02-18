lista_nombre=[]
nombre= input("INgrese el nombre del cliente. Para terminar escriba 'fin'. ").strip()

while nombre.lower() != "fin":
    
    if nombre != "":
       lista_nombre.append(nombre.title())
    else:
        print("El nombre está vacío. POr favor ingreselo nuevamente:")
    nombre= input("INgrese el nombre del cliente. Para terminar escriba 'fin'. ").strip()
    
lista_nombre.sort()
print("Lista de nombres ordenadas alfabeticamente. ")
print("*******************************************")
for nombres in lista_nombre:
    print( "         ",nombres)
print(" Primer cambio en archivo")


    

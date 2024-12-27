opcion = None
# Lista para almacenar productos
inventario = []

# Función para mostrar el menú
while opcion != 3 :
    print ("Menú Interactivo")
    print("")
    print("1. Agregar producto")
    print("2. Consultar productos")
    print ("3. Salir")
    print ("")
    opcion = int(input ("Seleccioná una opción del menú:"))

    if opcion == 1:
        # Agregar producto al inventario
        nombre = input("Ingrese el nombre del producto:")
        cantidad = int(input("Ingrese la cantidad del producto:"))
        inventario.append([nombre, cantidad])
        print("\nProducto agregado correctamente.\n")

    elif opcion == 2:
        # Mostrar inventario
        print("\nInventario actual:\n")
        if len(inventario) == 0:
            print("El inventario está vacío.")
        else:
            for producto in inventario:
                print("-", producto[0] + ":", producto[1], "unidades")

    elif Opcion==3:
         print("\nGracias por usar nuestra aplicación.\n")    
    else:
        print("\nOpción incorrecta\n")

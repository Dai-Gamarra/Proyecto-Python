import sqlite3 # Importa el módulo para interactuar con bases de datos SQLite

opcion = None # Variable para almacenar la opción seleccionada por el usuario

productos = [] 
 
 # Función para registrar nuevos productos en la base de datos
def registrar_productos():
 # conexión a la base de datos
    
    con = sqlite3.connect('inventario.db')
 # Crea un cursor para ejecutar comandos SQL
    cur = con.cursor() 
    
    # El usuario debe ingresar los datos del producto (los solicita y valida)

    while True:
        try:
            nombre = input("Ingrese el nombre del producto: ").strip()
            if not nombre:
                raise ValueError("El nombre no puede estar vacío.")
            
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                raise ValueError("La cantidad debe ser mayor o igual a 0.")
            
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                raise ValueError("El precio debe ser mayor o igual a 0.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

# Inserta el nuevo producto en la base de datos   
    cur.execute(f"INSERT INTO productos (nombre, cantidad, precio) values(?,?,?)", (nombre, cantidad, precio))
    
    con.commit() # Confirma los cambios en la base de datos
    
    con.close() # Cierra la conexión

# Función para mostrar todos los productos en la base de datos    
def mostrar_productos(): 
    
    con = sqlite3.connect("inventario.db")

    cur = con.cursor()

    cur.execute("SELECT * FROM productos")  # Consulta todos los productos
    
    productos = cur.fetchall() # Recupera los resultados de la consulta

    if not productos:
        print("\nNo hay productos registrados.\n")
    else:
        print("\nListado de Productos\n")
        for producto in productos:
            print("Id:", producto[0], "Nombre:", 
            producto[1], "Cantidad:", 
            producto[2], "Precio:", 
            producto[3])

    con.close()

    print("")
       
# Función para actualizar la cantidad de un producto
def actualizar_producto():

    print("\nActualización de Producto\n")
    
    mostrar_productos()  # Muestra los productos disponibles

    con = sqlite3.connect("inventario.db")

    cur = con.cursor()   

    id = int(input("Ingrese el id del producto a actualizar: "))   # Solicita el ID del producto
    nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: ")) # Solicita la nueva cantidad
# Actualiza la cantidad en la base de datos
    cur.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id))
    
    print("\nLa cantidad del producto fue actualizada\n")
    
    con.commit()
    con.close()
    

# Función para eliminar un producto
def eliminar_producto():
    try:
        con = sqlite3.connect("inventario.db")
        cur = con.cursor()
        
        mostrar_productos()
        id = int(input("Ingrese el id del producto que desea eliminar: ")) # Solicita el ID del producto
# Busca el producto por ID        
        cur.execute("SELECT nombre FROM productos WHERE id = ?", (id,))
        producto = cur.fetchone()
        if not producto:
            print("\nEl producto no existe.\n")
            return
# Confirma la eliminación del producto       
        confirmacion = input(f"¿Está seguro de eliminar el producto '{producto[0]}'? (s/n): ").lower()
        if confirmacion == "s":
            cur.execute(f"DELETE FROM productos WHERE id = {id}")
            con.commit() #confirma los cambios
            print("\nEl producto fue eliminado exitosamente.\n")
        else:
            print("\nOperación cancelada.\n")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    except ValueError:
        print("Entrada inválida.")
    finally:
        con.close()
 
# Función para buscar productos por nombre
def buscar_producto():
    print("\nBusqueda producto\n")
    
    nom = input("Ingrese el nombre del producto que desea consultar: ").strip()  #solicita el nombre del producto

    con = sqlite3.connect("inventario.db")
    
    cur = con.cursor()
# Busca productos cuyo nombre contenga el texto ingresado
    cur.execute(f"SELECT * FROM productos WHERE nombre like '%{nom}%'")
    productos = cur.fetchall()  # Recupera los resultados de la consulta
    
    if not productos:
        print("\nNo se encontraron productos.\n")
    else:
        print("\nResultados de la Búsqueda\n")
        for producto in productos:
            print("Id:", producto[0], "Nombre:", 
            producto[1], "Cantidad:", 
            producto[2], "Precio:", 
            producto[3])    
    
    con.close()
    
# Función para generar un reporte de productos con bajo stock
def reporte_bajo_stock():
    print("Reporte productos de bajo stock")

    limite = int(input("Ingrese la cantidad limite de bajo stock: ")) # Solicita el límite de cantidad

    con = sqlite3.connect("inventario.db")

    cur = con.cursor()
# Busca productos cuya cantidad sea menor o igual al límite
    cur.execute(f"SELECT * FROM productos WHERE cantidad <= {limite}")
    productos = cur.fetchall()  # Recupera los resultados de la consulta
    
    print("\nListado de Productos con Bajo Stock\n")
    
    for producto in productos:
        print("Id:", producto[0], "Nombre:", 
        producto[1], "Cantidad:", 
        producto[2], "Precio:", 
        producto[3])

    con.close()

    print("")

# Bucle principal del programa
while opcion != 7:
 try:
  # Menú de opciones
    print("Menú Interactivo")
    print("")
    print("1. Agregar producto")
    print("2. Consultar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reporte bajo stock")
    print("7. Salir")
    print("")

    opcion = int(input("Seleccioná una opción del menú: "))

    # Código que gestiona las opciones 
    
    if opcion == 1:
        registrar_productos()

    elif opcion == 2: 
        mostrar_productos()

    elif opcion == 3: 
        actualizar_producto()

    elif opcion == 4:
        eliminar_producto()

    elif opcion == 5:
        buscar_producto()

    elif opcion == 6:
        reporte_bajo_stock()

    elif opcion == 7:
        print("\nGracias por usar nuestra aplicación.\n")
    else:
        print("\nOpción Incorrecta\n")  
 except ValueError:
        print("\nPor favor, ingrese un número válido.\n")
inventario = {}

# Función para agregar un producto al inventario
def agregar_producto():
    producto = input("Ingrese el nombre del producto: ").lower()
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto {producto} agregado/actualizado con éxito.")

# Función para actualizar la cantidad de un producto existente
def actualizar_producto():
    producto = input("Ingrese el nombre del producto a actualizar: ").lower()
    if producto in inventario:
        nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {producto}: "))
        inventario[producto] = nueva_cantidad
        print(f"La cantidad del producto {producto} ha sido actualizada a {nueva_cantidad}.")
    else:
        print(f"Error: El producto {producto} no existe en el inventario.")

# Función para mostrar el inventario actual
def mostrar_inventario():
    if len(inventario) == 0:
        print("El inventario está vacío.")
    else:
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")

# Función principal
def main():
    while True:
        print("\n1. Agregar producto")
        print("2. Actualizar cantidad de producto")
        print("3. Mostrar inventario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            actualizar_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija una opción del 1 al 4.")

# Llamamos a la función principal
main()
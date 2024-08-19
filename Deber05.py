calificaciones = {}

# Función para pedir el nombre de un estudiante
def pedir_nombre_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    return nombre.strip().capitalize()

# Función para agregar o actualizar un estudiante y sus calificaciones
def agregar_o_actualizar_estudiante(nombre):
    notas = []
    while True:
        nota = input("Ingresa una nota para {} (o escribe 'fin' para terminar): ".format(nombre))
        if nota.lower() == 'fin':
            break
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    calificaciones[nombre] = notas
    print(f"Calificaciones de {nombre} actualizadas correctamente.")

# Función para buscar un estudiante y mostrar sus calificaciones
def buscar_estudiante(nombre):
    if nombre in calificaciones:
        print(f"Calificaciones de {nombre}: {calificaciones[nombre]}")
    else:
        print(f"No se encontró a ningún estudiante con el nombre {nombre}.")

# Función para actualizar las calificaciones de un estudiante existente
def actualizar_calificaciones(nombre):
    if nombre in calificaciones:
        print(f"Actualizando calificaciones para {nombre}. Las calificaciones actuales son: {calificaciones[nombre]}")
        agregar_o_actualizar_estudiante(nombre)
    else:
        print(f"No se encontró a ningún estudiante con el nombre {nombre}.")

# Función principal
def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar/Actualizar estudiante")
        print("2. Buscar estudiante")
        print("3. Actualizar calificaciones de un estudiante")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = pedir_nombre_estudiante()
            agregar_o_actualizar_estudiante(nombre)
        elif opcion == "2":
            nombre = pedir_nombre_estudiante()
            buscar_estudiante(nombre)
        elif opcion == "3":
            nombre = pedir_nombre_estudiante()
            actualizar_calificaciones(nombre)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Llamada a la función principal
main()
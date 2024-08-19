import math

# Variables globales para el umbral
umbral = 5.0

# Función para pedir las notas
def pedir_notas():
    notas = []
    while True:
        nota = input("Ingresa una nota (o escribe 'fin' para terminar): ")
        if nota.lower() == 'fin':
            break
        try:
            nota = float(nota)
            notas.append(nota)
        except ValueError:
            print("Por favor, ingresa un número válido.")
    return notas

# Función para filtrar notas por el umbral
def filtrar_notas(notas):
    notas_filtradas = []
    for nota in notas:
        if nota >= umbral:
            notas_filtradas.append(nota)
    return notas_filtradas

# Función para calcular el promedio
def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

# Función para calcular la varianza
def calcular_varianza(notas, promedio):
    if len(notas) == 0:
        return 0
    suma_diferencias_cuadradas = sum((nota - promedio) ** 2 for nota in notas)
    varianza = suma_diferencias_cuadradas / len(notas)
    return varianza

# Función principal
def main():
    notas = pedir_notas()
    notas_filtradas = filtrar_notas(notas)
    
    if len(notas_filtradas) == 0:
        print(f"Ninguna nota está por encima del umbral ({umbral}).")
    else:
        promedio = calcular_promedio(notas_filtradas)
        varianza = calcular_varianza(notas_filtradas, promedio)
        desviacion_estandar = math.sqrt(varianza)
        
        print(f"El promedio de las notas que están por encima del umbral ({umbral}) es: {promedio:.2f}")
        print(f"La varianza de las notas es: {varianza:.2f}")
        print(f"La desviación estándar de las notas es: {desviacion_estandar:.2f}")

# Llamada a la función principal
main()
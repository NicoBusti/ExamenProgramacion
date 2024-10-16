# main.py

from Funciones import *

def menu():
    print("1. Obtener existencias")
    print("2. Calcular total por depósito")
    print("3. Obtener artículos a reponer")
    print("4. Máxima cantidad de artículos almacenados de cada tipo")
    print("5. Corregir error de carga")
    print("6. Depósitos con más de 3.000.000 unidades")
    print("7. Porcentaje de artículos por tipo")
    print("8. Informe de recaudación")
    print("9. Depósito con mayor recaudación")
    print("0. Salir")

def main():
    existencias = []
    
    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            existencias = cargar_existencias()
        elif opcion == 2:
            total_por_deposito = calcular_total_por_deposito(existencias)
            print(total_por_deposito)
        elif opcion == 3:
            articulos_a_reponer = obtener_articulos_a_reponer(existencias)
            print(articulos_a_reponer)
        elif opcion == 4:
            maximos = max_articulos_por_tipo(existencias)
            print(maximos)
        elif opcion == 5:
            existencias = corregir_error_carga(existencias)
        elif opcion == 6:
            provincias = depositos_mas_3000000(existencias)
            print(provincias)
        elif opcion == 7:
            porcentajes = porcentaje_articulos(existencias)
            print(porcentajes)
        elif opcion == 8:
            recaudacion = calcular_total_por_deposito(existencias)  # Cambiar a recaudación real si se tiene
            recaudacion_ordenada = bubble_sort_recaudacion(recaudacion)
            print(recaudacion_ordenada)
        elif opcion == 9:
            precios = [100, 150, 200, 250, 300, 350, 400]  # Ejemplo de precios
            provincia_maxima, recaudacion_maxima = deposito_mayor_recaudacion(recaudacion, precios)
            print(f"Depósito con mayor recaudación: {provincia_maxima} con {recaudacion_maxima}")
        elif opcion == 0:
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()




# funciones.py

# 1

def cargar_existencias():
    """Cargar existencias de artículos en depósitos."""
    existencias = []
    provincias = ["PBA", "Jujuy", "Neuquén"]
    articulos = ["químicos", "trapos", "escobas", "cepillos", "papel higiénico", "jabón", "pañuelos descartables"]
    
    for provincia in provincias:
        fila = [provincia]
        for articulo in articulos:
            cantidad = int(input(f"Ingrese la cantidad de {articulo} en {provincia}: "))
            fila.append(cantidad)
        existencias.append(fila)
    
    return existencias

#2
def calcular_total_por_deposito(existencias):
    """Calcular la cantidad total de artículos almacenados por depósito."""
    totales = []
    for fila in existencias:
        total = sum(fila[1:])  # Sumar cantidades de artículos
        totales.append((fila[0], total))
    return totales

#3
def obtener_articulos_a_reponer(existencias, umbral=3000):
    """Obtener artículos que necesitan ser repuestos."""
    articulos_a_reponer = []
    for fila in existencias:
        provincia = fila[0]
        for i in range(1, len(fila)):
            if fila[i] < umbral:
                articulos_a_reponer.append((provincia, i))
    return articulos_a_reponer

#4
def max_articulos_por_tipo(existencias):
    """Calcular la máxima cantidad de artículos de cada tipo y su provincia."""
    maximos = {}
    for i in range(1, len(existencias[0])):
        max_cantidad = 0
        provincia_maxima = ""
        for fila in existencias:
            if fila[i] > max_cantidad:
                max_cantidad = fila[i]
                provincia_maxima = fila[0]
        maximos[i] = (max_cantidad, provincia_maxima)
    return maximos

#5
def corregir_error_carga(existencias):
    """Corregir un error de carga aleatoria o distribuida."""
    for fila in existencias:
        for i in range(1, len(fila)):
            fila[i] = int(input(f"Ingrese la cantidad corregida para {fila[0]} - artículo {i}: "))
    return existencias

#6
def depositos_mas_3000000(existencias):
    """Cantidad de depósitos que han almacenado más de 3.000.000 unidades."""
    provincias = []
    for fila in existencias:
        total = sum(fila[1:])
        if total > 3000000:
            provincias.append(fila[0])
    return provincias

#7
def porcentaje_articulos(existencias):
    """Calcular el porcentaje de artículos de cada tipo sobre el total."""
    totales = calcular_total_por_deposito(existencias)
    total_general = sum(total for _, total in totales)
    
    porcentajes = []
    for i in range(1, len(existencias[0])):
        cantidad = sum(fila[i] for fila in existencias)
        porcentaje = (cantidad / total_general) * 100 if total_general > 0 else 0
        porcentajes.append((i, porcentaje))
    return porcentajes

#8
def bubble_sort_recaudacion(recaudacion):
    """Ordenar la recaudación de cada depósito usando bubble sort."""
    n = len(recaudacion)
    for i in range(n):
        for j in range(0, n-i-1):
            if recaudacion[j][1] < recaudacion[j+1][1]:  # Ordenar de mayor a menor
                recaudacion[j], recaudacion[j+1] = recaudacion[j+1], recaudacion[j]
    return recaudacion

#9
def deposito_mayor_recaudacion(recaudacion, precios):
    """Determinar el depósito con mayor recaudación."""
    max_recaudacion = 0
    provincia_maxima = ""
    
    for i, (provincia, cantidad) in enumerate(recaudacion):
        total_recaudacion = cantidad * precios[i]
        if total_recaudacion > max_recaudacion:
            max_recaudacion = total_recaudacion
            provincia_maxima = provincia
    
    return provincia_maxima, max_recaudacion

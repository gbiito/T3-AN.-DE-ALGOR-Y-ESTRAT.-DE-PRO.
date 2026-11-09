import random
import math

def calcular_monte_carlo():
    print("=== MÉTODO DE MONTE CARLO: INTERSECCIÓN ELIPSE E HIPÉRBOLA ===")
    
    a = float(input("Ingrese el valor de a (para la elipse): "))
    b = float(input("Ingrese el valor de b (para la elipse): "))
    c = float(input("Ingrese el valor de c (para la hipérbola): "))
    d = float(input("Ingrese el valor de d (para la hipérbola): "))
    cantidad = int(input("Ingrese la cantidad de puntos aleatorios: "))

    puntos_elipse = 0
    puntos_interseccion = 0

    for _ in range(cantidad):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)

        en_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1

        if en_elipse:
            puntos_elipse += 1

            en_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1

            if en_hiperbola:
                puntos_interseccion += 1

    area_elipse_teorica = math.pi * a * b

    if puntos_elipse > 0:
        area_interseccion = area_elipse_teorica * (puntos_interseccion / puntos_elipse)
    else:
        area_interseccion = 0.0

    print("\n" + "="*40)
    print("RESULTADOS DE LA SIMULACIÓN:")
    print(f"1. Puntos aleatorios dentro de la elipse: {puntos_elipse}")
    print(f"2. Puntos en la intersección (elipse e hipérbola): {puntos_interseccion}")
    print(f"3. Área aproximada de la zona de intersección: {area_interseccion:.4f}")
    print("="*40)

if __name__ == "__main__":
    calcular_monte_carlo()
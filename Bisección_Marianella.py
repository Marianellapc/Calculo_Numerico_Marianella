import math

def bisection_method(f, a, b, tolerance, max_iterations):
   
    for i in range(max_iterations):
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            print(f"Iteración {i+1}: Raíz aproximada: {c}, f(c): {f(c)}")
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        print(f"Iteración {i+1}: Intervalo: [{a}, {b}]")

    print(f"No se encontró una raíz dentro de la tolerancia especificada después de {max_iterations} iteraciones.")
    return None

if __name__ == "__main__":
    # Define la función
    f = lambda x: math.exp(x) - 3 * (x*2)

    # Define el intervalo y los parámetros
    a = 0
    b = 1
    tolerance = 0.05
    max_iterations = 20

    # Ejecuta el método de bisección
    root = bisection_method(f, a, b, tolerance, max_iterations)
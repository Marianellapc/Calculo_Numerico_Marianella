import math

def derivada(f, h = 0.02):
    """
    Calcula la derivada numérica de la función f usando la aproximación de diferencias finitas.
    """
    def _(x):
        return (f(x + h) - f(x))/h
    return _

def newton_raphson(f, x0, tolerance, max_iterations):

    for i in range(max_iterations):
        x1 = x0 - f(x0) / derivada(f)(x0)  # Calcula la siguiente aproximación
        error = abs(x1 - x0)  # Calcula el error relativo

        print(f"Iteración {i+1}: Aproximación: {x1: .4f}, Error: {error: .4f}")
        
        if error < tolerance:
            print("======================================================================")
            return x1

        x0 = x1  # Actualiza la aproximación inicial

    print(f"No se encontró una raíz dentro de la tolerancia especificada después de {max_iterations} iteraciones.")
    return None

if __name__ == "__main__":
    # Define la función
    f = lambda x: math.sin(x) - math.exp(-x)

    # Define la aproximación inicial y los parámetros
    x0 = 0.5
    tolerance = 0.02
    max_iterations = 10

    # Ejecuta el método de Newton-Raphson
    root = newton_raphson(f, x0, tolerance, max_iterations)
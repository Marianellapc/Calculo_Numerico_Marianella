import math

def derivada(f, h=0.01):
    """
    Calcula la derivada numérica de la función f usando la aproximación de diferencias finitas.
    """
    def _(x):
        return (f(x + h) - f(x)) / h
    return _

def polinomio_taylor(f, x0, n):
    """
    Construye el polinomio de Taylor de grado n para la función f en el punto x0.
    """
    def polinomio(x):
        """
        Evalúa el polinomio de Taylor en el punto x.
        """
        p = f(x0)
        for i in range(1, n + 1):
            d = derivada(f)  # Calcula la derivada de orden i
            for _ in range(i - 1):  # Calcula derivadas sucesivas
                d = derivada(d)
            p += (d(x0) * (x - x0)*i) / math.factorial(i)
        return p
    return polinomio

f1 = lambda x: x*2 + math.cos(x)

def view_result_polinomio(f, x, x0, n):
    """
    Muestra el resultado del polinomio de Taylor y lo compara con el valor real.
    """
    poli = polinomio_taylor(f, x0, n)
    valor_aproximado = poli(x)
    valor_real = f(x)
    error_relativo = abs(valor_real - valor_aproximado)

    print(f"Valor Aproximado: {valor_aproximado:.4f} "
          f"Valor Real: {valor_real:.4f} "
          f"Error Relativo: {error_relativo:.4f}")
    print("======================================================================")
    return valor_aproximado

if __name__ == '__main__':
    view_result_polinomio(f1, 0.3, 0, 3)
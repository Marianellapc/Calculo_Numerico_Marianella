import math

def integral_Rieman(f, a, b, n):
   
    h = (b - a) / n  # Ancho de cada subintervalo
    suma = 0
    for i in range(n):
        xi = a + i * h  # Punto medio del i-ésimo subintervalo
        suma += f(xi) * h  # Suma de las áreas de los rectángulos

    return suma

f1 = lambda x: x / (x*2 + 1)

def view_result_Rieman(f, a, b, n):
  
    area = integral_Rieman(f, a, b, n)
    print(f"Valor aproximado: {area:.4f}")
    print("======================================================================")
    return area

if __name__ == '__main__':
    view_result_Rieman(f1, 0, 1, 4)
import math

def trapezoid_method(f, a, b, n):
   
    h = (b - a) / n  # Ancho de cada subintervalo
    area = 0
    for i in range(n):
        x0 = a + i * h
        x1 = a + (i + 1) * h
        area += (h / 2) * (f(x0) + f(x1))  # Suma de las áreas de los trapecios

    return area

f1 = lambda x: x * math.cos(x*2)

def view_result_trapeze(f, a, b, n):
   
    area = trapezoid_method(f, a, b, n)
    print(f"Valor aproximado: {area:.4f}")
    print("======================================================================")
    return area

if __name__ == '__main__':
    view_result_trapeze(f1, 0, 1, 4)
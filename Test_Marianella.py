import unittest
import math
from Bisección_Marianella import bisection_method
from newton_rhapson_Marianella import newton_raphson
from Taylor_Marianella import view_result_polinomio
from rieman_Marianella import view_result_Rieman
from Trapecio_Marianella import view_result_trapeze

class TestMetodosNumericos(unittest.TestCase):
    """
    Conjunto de pruebas unitarias para los métodos numéricos implementados.
    """

    def test_biseccion_method(self):
        """
        Prueba el método de bisección con diferentes funciones y valores esperados.
        """
        print("nn==========  METODO DE BISECCIÓN  ====================================")
        f1 = lambda x: math.exp(-x) - math.log(x)
        f2 = lambda x: (x - 2)**2 - math.log(x)
        f3 = lambda x: math.sin(x) - math.exp(-x)
        f4 = lambda x: (x + 1)**0.5 - math.tan(x)
        self.assertEqual(bisection_method(f1, 1, 1.5, 0.05, 20), 1.3125)
        self.assertEqual(bisection_method(f2, 1, 2, 0.05, 20), 1.4375)
        self.assertEqual(bisection_method(f3, 0, 1, 0.04, 20), 0.5625)
        self.assertEqual(bisection_method(f4, 0.5, 1, 0.01, 20), 0.94921875)

    def test_newton_raphson_method(self):
        """
        Prueba el método de Newton-Raphson con diferentes funciones y valores esperados.
        """
        print("nn==========  METODO DE NEWTHON RAPHSON  ===============================")
        f1 = lambda x: math.exp(x) - 2 * x**2
        f2 = lambda x: (x - 2)**2 - math.log(x)
        f3 = lambda x: math.sin(x) - math.exp(-x)
        self.assertAlmostEqual(newton_raphson(f1, 0.5, 0.02, 10), 2.617981245646947, places=4)  # Ajuste para comparar con precisión
        self.assertAlmostEqual(newton_raphson(f2, 1, 0.05, 20), 1.4124215461418443, places=4)
        self.assertAlmostEqual(newton_raphson(f3, 0.5, 0.02, 10), 0.5885488916184832, places=4)

    def test_polinomio_taylor_method(self):
        """
        Prueba el polinomio de Taylor con diferentes funciones y valores esperados.
        """
        print("nn==========  POLINOMIO DE TAYLOR  =====================================")
        f1 = lambda x: math.exp(x)
        f3 = lambda x: x*2 + math.cos(x)
        self.assertAlmostEqual(view_result_polinomio(f1, 1, 0, 5), 3.735397235264392, places=4)
        self.assertAlmostEqual(view_result_polinomio(f3, 1, 0, 3), 2.0025579991709277, places=4)

    def test_Rieman_method(self):
        """
        Prueba el método de Riemann con diferentes funciones y valores esperados.
        """
        print("nn==========  METODO DE RIEMAN  ========================================")
        f1 = lambda x: x / (x**2 + 1)
        f2 = lambda x: x * (x**2 + 1)**0.5
        self.assertAlmostEqual(view_result_Rieman(f1, 0, 1, 4), 0.2788235294117647, places=4)
        self.assertAlmostEqual(view_result_Rieman(f2, 1, 2, 4), 2.4116477770123668, places=4)

    def test_trapezoid_method(self):
        """
        Prueba el método del trapecio con diferentes funciones y valores esperados.
        """
        print("nn==========  METODO DEL TRAPECIO  =====================================")
        f1 = lambda x: x * math.cos(x**2)
        f2 = lambda x: math.sin(x) - x**2
        self.assertAlmostEqual(view_result_trapeze(f1, 0, 1, 4), 0.4096406539719295, places=4)
        self.assertAlmostEqual(view_result_trapeze(f2, 0, 1, 4), 0.1135509375715020, places=4)


if __name__ == '__main__':
    unittest.main()
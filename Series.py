# series.py
"""
Módulo de Series
Autor: Hinojosa Viteri Kevin Steven 
Fecha: 26/01/2025
"""

def serie_fibonacci(n):
    """
    Genera una serie Fibonacci hasta el término n
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
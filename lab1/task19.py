import numpy as np
import sympy as sp

def left_rectangle(f, x, h):
    new_X = np.linspace(0, x, np.ceil(x / h).astype(np.int64) + 1)
    estimated_value = h * np.sum(f(new_X[1:-1]))
    return estimated_value

def task_19():
    """
    19. Наближено обчислити iнтеграл I = int_0^1 e^x/sqrt(x) dx методом Канторовича. Використати квадратурну формулу лiвих прямокутникiв.
    """
    print("Starting Task 19")
    x = sp.Symbol('x')
    phi = sp.exp(x)
    alpha = 0.5
    order = 5
    range_end = 1
    taylor_series = sp.series(phi, x, 0, order).removeO()
    psi = phi - taylor_series

    I_1 = (taylor_series / x**alpha).as_poly()

    degrees = [i.args[1] for i in I_1.args[1:]]
    I_1_value = 0
    for deg, coeff in zip(degrees, I_1.coeffs()):
        I_1_value += coeff / (1 + deg) * range_end ** (1 + deg)
    print("I_1:", I_1_value)

    I_2 = sp.lambdify(x, psi, 'numpy')
    I_2_value = left_rectangle(I_2, range_end, 10e-5)
    print("I_2:", I_2_value)

    print("Result:", I_1_value + I_2_value)
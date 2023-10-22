import numpy as np

def right_rectangle(f, start, x, h):
    new_X = np.linspace(start, x, np.ceil(x / h).astype(np.int64) + 1)
    estimated_value = h * np.sum(f(new_X[1:]))
    return estimated_value

def func(x):
    return 1 / (1 + x**3)

def deriv(x):
    return -3 * x**2 / (1 + x**3)**2

def task_32():
    """
     Наближено обчислити iнтеграл I = int_2^inf 1/(1+x^3) dx за допомогою методу обрiзання границь з точнiстю ε = 0,005. Використати метод правих прямокутникiв, оцiнку залишкових членiв.
    """
    epsilon = 0.005
    R = epsilon / 2
    I_2 = R
    start = 2
    A = 400
    M_1 = np.abs(deriv(1/(2**(1/3))))
    h = 2 * R / (M_1 * (A - start))
    I_1 = right_rectangle(func, start, A, h)
    estimation = I_1 + I_2
    real_value = 0.1191978
    print(estimation)
    print(real_value)
    print(estimation - real_value)
    
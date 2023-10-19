import numpy as np
import matplotlib.pyplot as plt

def find_position_of_first_non_zero(number):
    if number == 0:
        return 0

    coefficient = abs(number)
    position = 0

    while coefficient < 1:
        coefficient *= 10
        position -= 1

    while coefficient >= 10:
        coefficient /= 10
        position += 1

    return position

def func(x):
    return -np.log(np.cos(x))

def left_rectangle(f, x, h):
    new_X = np.linspace(0, x, np.ceil(x / h).astype(np.int64) + 1)
    estimated_value = h * np.sum(f(new_X[:-1]))
    return estimated_value


def task_6():
    """
    6. Побудувати таблицi функцiї Лобачевського з 2 правильними значущими цифрами на промiжку [0; π/2] з кроком π/36, побудувати графiк функцiї. Використати формулу лiвих прямокутникiв, оцiнку залишкових членiв.
    """
    real_values = [
        0, 0.00011084649214, 0.0008888111339, 0.003011343601, 0.007177208015,
        0.014118858118, 0.02461714625, 0.03951967161, 0.05976470441, 
        0.08641372549, 0.12069761248, 0.1640852806, 0.2183912269, 0.2859552204, 
        0.3699685268, 0.4751379721, 0.6092925921, 0.7886651626, 1.088793045
    ]

    X, step = np.linspace(0, np.pi / 2, 19, retstep=True)
    estimations = []
    diffs = []
    for i, x in enumerate(X):
        pre_h = step / 16
        pre_estimation = left_rectangle(func, x, pre_h)
        R = 10 ** (find_position_of_first_non_zero(pre_estimation) - 1) / 2
        M_1 = 0
        h = 0
        if x != 0:
            M_1 = np.tan(x)
            j = 10
            while M_1 > 20 and j > 0:
                M_1 = np.tan(x - 10 ** (-j))
                j -= 1
            h = 2 * R / (M_1 * x)
            estimation = left_rectangle(func, x, h)
        else:
            estimation = pre_estimation

        estimations += [estimation]
        diff = real_values[i] - estimation
        diffs += [diff]
        print("x: ", x)
        print("pre_Value: ", f'{pre_estimation:.10f}')
        print("Value: ", f'{estimation:.10f}')
        print("Real value: ", f'{real_values[i]:.10f}')
        # print("M_1: ", f'{M_1:.10f}')
        print("R: ", f'{R:.10f}')
        # print("R_with_pre: ", f'{M_1 * x * pre_h / 2:.10f}')
        # print("pre_h: ", f'{pre_h:.10f}')
        # print("h: ", f'{h:.10f}')
        print("Difference: ", f'{diff:.10f}')
        print("=====================================")
    
    fig, ax = plt.subplots()
    ax.plot(X, estimations, marker='o', linestyle='-', label='Estimation', color='blue')
    ax.plot(X, real_values, marker='o', linestyle='-', label='Real values', color='red')
    ax.plot(X, diffs, marker='o', linestyle='-', label='Diffs', color='green')

    # Add labels and a title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Lobachevsky function')

    # Add a legend
    ax.legend()

    plt.grid(True)

    custom_xticks = [i * np.pi / 36 for i in range(19)]  # Custom tick positions
    custom_xticklabels = [f'{i}pi/{36}' for i in range(19)]  # Custom tick labels
    ax.set_xticks(custom_xticks)
    ax.set_xticklabels(custom_xticklabels, rotation=45, fontsize=8) 

    custom_yticks = real_values
    custom_yticklabels = [f'{yi:.2f}' for yi in y1]
    ax.set_yticks(custom_yticks)
    ax.set_yticklabels(custom_yticklabels)

    # Display the plot
    plt.show()
# TODO: import ...
import numpy as np
import matplotlib.pyplot as plt

def generate_random_matrix(m, n):
    return np.random.randint(0,2,(m,n))
    # raise NotImplementedError  # TODO: 删除该行，实现该函数功能


def save_matrix(matrix, file_name):
    plt.plot(matrix)
    plt.savefig(file_name)
    plt.show()
    # raise NotImplementedError  # TODO: 删除该行，实现该函数功能


if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")
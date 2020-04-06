import sys
import numpy as np


def read_input_pizza(filename):
    """Reads the input of the pizza problem

    returns:

    M: number of maximum pizza slices
    N: number different types of pizza
    available: number of slices in each type, non-decreasing order
    """
    lines = open(filename).readlines()
    M, N = [int(val) for val in lines[0].split()]
    available = np.array([int(n) for n in lines[1].split()])
    return M, N, available


def main():
    if(len(sys.argv) != 3):
        print('oops')
        return BufferError

    filename = sys.argv[2]
    M, N, available = read_input_pizza(filename)


if __name__ == "__main__":
    main()

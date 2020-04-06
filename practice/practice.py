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


def greedy(M, N, available):
    available = np.flip(available)
    typeQuantity = np.zeros(available.size)

    for i in range(len(available)):
        if(M-available[i] >= 0 and typeQuantity[i] == 0):
            typeQuantity[i] = 1
            M = M - available[i]

    typeQuantity = np.flip(typeQuantity)
    return typeQuantity


def naive(M, N, available):
    typeQuantity = np.zeros(available.size)

    for i in range(len(available)):
        if(M-available[i] >= 0 and typeQuantity[i] == 0):
            typeQuantity[i] = 1
            M = M - available[i]

    return typeQuantity


def random(M, N, available):
    np.random.shuffle(available)
    typeQuantity = np.zeros(available.size)

    for i in range(len(available)):
        if(M-available[i] >= 0 and typeQuantity[i] == 0):
            typeQuantity[i] = 1
            M = M - available[i]

    return typeQuantity


def sneaky(M, N, available):

    solutionIndexList = []
    solutionValueList = []
    currentIndexList = []
    currentValueList = []
    fullSize = len(available)
    maxScore = 0
    startIndex = fullSize
    sum = 0

    while((len(currentIndexList) > 0 and currentIndexList[0] != 0) or len(currentIndexList) == 0):

        startIndex = startIndex - 1

        for i in range(startIndex, -1, -1):

            currentValue = available[i]
            tempSum = sum + currentValue

            if (tempSum == M):
                sum = tempSum
                currentIndexList.append(i)
                currentValueList.append(currentValue)
                break
            elif (tempSum > M):
                continue

            elif (tempSum < M):
                sum = tempSum
                currentIndexList.append(i)
                currentValueList.append(currentValue)
                continue

        if (maxScore < sum):
            maxScore = sum

            solutionIndexList = []
            solutionValueList = []

            for y in currentIndexList:
                solutionIndexList.append(y)
            for y in currentValueList:
                solutionValueList.append(y)

        if (maxScore == M):
            break

        if(len(currentValueList) != 0):
            lastVal = currentValueList.pop()
            sum = sum - lastVal

        if(len(currentIndexList) != 0):
            lastIndex = currentIndexList.pop()
            startIndex = lastIndex

        if(len(currentIndexList) == 0 and (startIndex == 0)):
            break

    # Print the score of the best solution
    print("SCORE = " + str(maxScore))

    return solutionIndexList


def main():
    if(len(sys.argv) != 3):
        print('oops')
        return BufferError

    filename = sys.argv[2]
    M, N, available = read_input_pizza(filename)

    func = sys.argv[1]

    res = globals()[func](M, N, available)

    if (func != 'sneaky'):
        num_types = np.sum(res)
        types = []
        for x in range(len(res)):
            if(res[x] == 1):
                types.append(x)
    else:
        num_types = len(res)
        types = res

    output = filename + '.out.txt'
    f = open(output, "w+")
    f.write('%d\n' % num_types)
    for i in types:
        f.write('%d ' % i)

    f.close()


if __name__ == "__main__":
    main()

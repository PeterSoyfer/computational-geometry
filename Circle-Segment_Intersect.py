# task_2.1.12_Soyfer

# import numpy as np

eps = 1e-15


def signum(x):
    if x > 1e-15:
        return 1
    elif x < -1e-15:
        return -1
    else:
        return 0


def length(x):  # Euclidian distance
    try:
        l = (x[0]**2 + x[1]**2)**0.5
    except OverflowError:
        print('\nWe got an OVERFLOW here\n')
        return -1
    else:
        return l  # np.sqrt(x@x)


def scalar(x, y):
    #try:
    c = x[0]*y[0]+x[1]*y[1]
    #except OverflowError:
    #    print('too much')
    #    return -1
    #else:
    return c


def ht(v1, v2, v3):
    #try:
    h = abs(v1[0]*v2[1]-v1[1]*v2[0])/length(v3)
    #except OverflowError:
    #    print('too much')
    #    return -1
    #else:
    return h


def dist(A, B, M): # a[0] == AB, a[1] == BA, c[0] == AM, c[1] == BM;
    # a = np.array([B-A, A-B])
    # c = np.array([M-A, M-B])
    a = [[B[0]-A[0], B[1]-A[1]], [A[0]-B[0], A[1]-B[1]]]
    c = [[M[0]-A[0], M[1]-A[1]], [M[0]-B[0], M[1]-B[1]]]
    sm = 0
    check = [a, c]
    for v in check:
        for k in range(2):
            if length(v[k]) == -1:
                return -1

    for k in range(2):
        m = scalar(a[k], c[k])
        sm += signum(m)
        if m <= eps:
            h = length(c[k])
    if sm == 2:
        h = ht(c[0], c[1], a[0])
    return h


def isintersected(M, r, A, B):  # M - center of circle, r - radius, A,B - ends of segment

    MA = [A[0]-M[0], A[1]-M[1]]
    MB = [B[0]-M[0], B[1]-M[1]]
    AB = [B[0]-A[0], B[1]-A[1]]

    if length(AB) == -1:
        print('\nWe got an OVERFLOW here\n')
        return -1

    elif length(AB) <= eps:  # segment with very close ends is considered as one point
        h = length(MA)  # catching the case of division by zero in dist() func
    else:
        h = dist(A, B, M)  # distance from M to AB
        if h == -1:
            print('\nWe got an OVERFLOW here\n')
            return -1

    a = length(MA)  # MA length
    b = length(MB)  # MB length

    if a == -1 or b == -1:
        print('\nWe got an OVERFLOW here\n')
        return -1

    if h > r:
        print("\nZero Points")
        return 0

    if abs(h-r) <= eps:  # h == r
        print("\nOne Point")
        return 1

    if h < r:
        if (abs(a-r) <= eps and abs(b-r) <= eps) or (abs(a-r) <= eps and b > r) or (abs(b-r) <= eps and a > r):
            # (a == b == r) or (a == r and b > r) or (b == r and a > r)
            print("\nTwo Points")
            return 2
        elif (abs(a-r) <= eps and b < r) or (abs(b-r) <= eps and a < r):
            # (a == r and b < r) or (b == r and a < r)
            print("\nOne Point")
            return 1

        if a < r and b < r:
            print("\nZero Points")
            return 0

# main programme


def main():
    arr = []
    try:
        with open(input('File: '), 'r') as f:
            for line in f:
                for x in line.split():
                    try:
                        if str(float(x)) == 'inf' or str(float(x)) == '-inf' or str(float(x)) == 'nan':
                            print('\nx is out of real numbers (NaN or +-inf)\n')
                            return -8
                        elif abs(float(x)) < eps and float(x) != 0:
                            print('\nUNDERFLOW\n')
                            return -9
                        else:
                            arr.append(float(x))
                    except OverflowError:
                        print('\nOVERFLOW\n')
                        return -1000
                    except ValueError:
                        print('\nWe got a ValueError here\n')
                        return -17
    except FileNotFoundError:
        print('\nFile not found\n')
        return 404
    if len(arr) >= 7:
        center = [arr[0], arr[1]]
        radius = arr[2]
        left = [arr[3], arr[4]]
        right = [arr[5], arr[6]]
        isintersected(center, radius, left, right)
        return
    else:
        print('\nNot enough data\n')
        return -1


main()

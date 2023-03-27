import numpy as np

N = None

def parseArrs(line: str, N: int) -> np.ndarray:
    arr = []
    strs = line.split(" ")

    for s in strs:
        num = float(s)
        arr.append(num)

    return np.array(arr)

def solution(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    global N
    N = len(b)
    x = np.zeros(N)
    #forward
    alpha, beta = [- c[0] / b[0]], [d[0] / b[0]]
    for i in range(1, N):
        if i != N-1:
            y = a[i-1] * alpha[i-1] + b[i]
            alpha.append(-c[i] / y)
            beta.append((d[i]-a[i-1] * beta[i-1]) / y)
        else:
            y = a[N-2] * alpha[N-2] + b[N-1]
            beta.append((d[N-1] - a[N-2] * beta[N-2]) / y)
    #backwards
    for i in reversed(range(N)):
        if i == N-1:
            x[N-1] = beta[N-1]
        else:
            x[i] = alpha[i] * x[i+1] + beta[i]
    return x

def makeMatrix(c: np.ndarray, b: np.ndarray, a: np.ndarray) -> np.ndarray:
    m = np.zeros((N,N))
    for i in range(N):
        for j in range(N):
            if i == j:
                m[i][j] = b[i]
                if i != N-1:
                    m[i][i+1] = c[i]
                    m[i+1][i] = a[i]
    return m

def mulMatVec(matrix: np.ndarray, x: np.ndarray) -> np.ndarray:
    d = np.zeros(N)
    for i in range(N):
        s = 0
        for j in range(N):
            s += matrix[i][j] * x[j]
        d[i] = s
    return d

def main():
    global N
    # tets<i>.txt = dimension; matrix: main diagonal, above diagonal , under diagonal; vector D
    with open("test1.txt") as file:
        N = int(file.readline().strip())
        arrs = [file.readline().strip() for _ in range(4)]

    b = parseArrs(arrs[0], N)
    c = parseArrs(arrs[1], N-1)
    a = parseArrs(arrs[2], N-1)
    d = parseArrs(arrs[3], N)

    x = solution(a, b, c, d)

    m = makeMatrix(c, b, a)
    # np.set_printoptions(precision=16)
    f = np.array2string(m, prefix="    ", suppress_small=True, formatter={'float_kind':lambda x: "%.8f" % x})

    #print(f"A = {f}\n")

    print("X: ", end="")
    print(" ".join([f"{n:.16f}" for n in x]))

    d_new = mulMatVec(m, x)
    print("new vector d: ", end="")
    print(" ".join([f"{n:.16f}" for n in d_new]))

    r = [np.abs(d[i] - d_new[i]) for i in range(N)]
    print("vector r: ", r)
    #print("A^(-1) = ", np.linalg.inv(m))
    e = mulMatVec(np.linalg.inv(m), r)
    f = np.array2string(e, prefix="    ", suppress_small=True, formatter={'float_kind': lambda x: "%.16f" % x})
    print(f"Погрешность : vector e = {f}")

    ans = [1, 1, 1, 1]
    #print(f"|x-x*| = : {abs(ans - x)}")

main()
import math

SIZE = 10

def f(x):
    return math.exp(x)

def direct(b, a, c, d, size):
    alpha = [-c[0] / b[0]]
    beta = [d[0] / b[0]]
    y = 0.0
    for i in range(1, size - 1):
        y = a[i - 1] * alpha[i - 1] + b[i]
        alpha.append(-c[i] / y)
        beta.append((d[i] - a[i - 1] * beta[i - 1]) / y)
    y = a[size - 2] * alpha[size - 2] + b[size - 1]
    beta.append((d[size - 1] - a[size - 2] * beta[size - 2]) / y)
    return alpha, beta

def reverse(alpha, beta, size):
    x = [0.0] * size
    x[size - 1] = beta[size - 1]
    for i in range(size - 2, -1, -1):
        x[i] = alpha[i] * x[i + 1] + beta[i]
    return x

def main():
    l, r = 0, 1
    h = (r - l) / SIZE
    xs = [l + i * h for i in range(SIZE + 1)]
    ys = [f(xs[i]) for i in range(SIZE + 1)]

    d = [3 * (ys[i + 1] - 2 * ys[i] + ys[i - 1]) / (h ** 2) for i in range(1, SIZE)]
    b = [4] * (SIZE - 1)
    a = [1] * (SIZE - 2)
    c = [1] * (SIZE - 2)

    alpha, beta = direct(b, a, c, d, SIZE - 1)
    coefC = reverse(alpha, beta, SIZE - 1)
    coefC.insert(0, 0)
    coefC.append(0)

    coefA = ys[:-1]
    coefB = [(ys[i + 1] - ys[i]) / h - (h / 3) * (coefC[i + 1] + 2 * coefC[i]) for i in range(SIZE)]
    coefD = [(coefC[i + 1] - coefC[i]) / (3 * h) for i in range(SIZE)]

    # погрешность сопоставима с вычислительной
    print("\nInterpolation nodes:")
    for i in range(SIZE):
        varX = l + i * h
        varY = f(varX)
        s = coefA[i] + coefB[i] * (varX - xs[i]) + coefC[i] * (varX - xs[i]) ** 2 + coefD[i] * (varX - xs[i]) ** 3
        print(f"x: {varX:.1f}, y: {varY:.16f}, y*: {s:.16f}, |y-y*|: {abs(varY - s):.16f}")

    print("\nIn the middles of interpolation nodes:")
    for i in range(SIZE):
        varX = l + (i + 0.5) * h
        varY = f(varX)
        s = coefA[i] + coefB[i] * (varX - xs[i]) + coefC[i] * (varX - xs[i]) ** 2 + coefD[i] * (varX - xs[i]) ** 3
        print(f"x: {varX:.2f}, y: {varY:.16f}, y*: {s:.16f}, |y-y*|: {abs(varY - s):.16f}")


main()
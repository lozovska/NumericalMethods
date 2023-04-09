import math

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

def f(x):
    return 3 * math.sin(2 * x)

def analytical(x):
    return (2 - 0.75 * x) * math.cos(2 * x) + 1.5 * math.sin(x) * math.cos(x)

p = 0.0
q = 4.0
a = analytical(0)
b = analytical(1)

print("МЕТОД ПРОГОНКИ:")
print("y'' + %0.1fy' + %0.1fy = (2 - 0.75*x)*cos(2x) + 1.5*sin(x)*cos(x)" % (p, q))
print("y(0) = %f" % a)
print("y(1) = %f" % b)

n = 40
h = 1.0 / float(n)
xs = [i * h for i in range(n + 1)]

as_ = [1 - h / 2 * p for i in range(n - 2)]
bs = [h * h * q - 2 for i in range(n - 1)]
cs = [1 + h / 2 * p for i in range(n - 2)]
ds = [h * h * f(0) - a * (1 - h / 2 * p)]

for i in range(2, n):
    ds.append(h * h * f(i * h))
ds[-1] = h * h * f((len(ds) - 1) * h) - b * (1 + h / 2 * p)

alpha, beta = direct(bs, as_, cs, ds, len(ds))
ys = [a] + reverse(alpha, beta, len(ds)) + [b]

maxR = 0.0
for i in range(0, len(ys), 4):
    inaccuracy = abs(ys[i] - analytical(xs[i]))
    print("x=%.1f, y=%.6f, y*=%.6f  |y-y*|=%.6f" % (i * h, analytical(xs[i]), ys[i], inaccuracy))
    if inaccuracy > maxR:
        maxR = inaccuracy

print("||y-y*||=%.6f" % maxR)

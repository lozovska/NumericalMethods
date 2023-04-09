import math

def f(x):
    return 3 * math.sin(2 * x)

def analytical(x):
    return (2 - 0.75 * x) * math.cos(2 * x) + 1.5 * math.sin(x) * math.cos(x)

n = 10
p = 0.0
q = 4.0
a = analytical(0)
b = analytical(1)
ys = [[], []]

def getC1():
    return (b - ys[0][n]) / ys[1][n]

def getYi(i):
    return ys[0][i] + getC1() * ys[1][i]

print("МЕТОД СТРЕЛЬБЫ:")
print("y'' + %0.1fy' + %0.1fy = (2 - 0.75*x)*cos(2x) + 1.5*sin(x)*cos(x)" % (p, q))
print("y(0) = %f" % a)
print("y(1) = %f" % b)
print("Количество разбиений: %d" % n)
h = 1.0 / float(n)
print(h)

delta = h * 100
xs = []
for i in range(n + 1):
    xs.append(float(i) * h)
for i in range(2):
    ys[i] = [a, a + delta]
ys[1] = [0, delta]

for i in range(1, n):
    ys[0].append((h * h * f(xs[i]) + (2.0 - q * h * h) * ys[0][i] - (1.0 - h / 2 * p) * ys[0][i - 1]) / (1 + h / 2 * p))
    ys[1].append(((2.0 - q * h * h) * ys[1][i] - (1.0 - h / 2 * p) * ys[1][i - 1]) / (1 + h / 2 * p))

y = []
for i in range(n + 1):
    y.append(getYi(i))
print(len(y))

maxR = 0.0

for i in range(len(y)):
    print("x=%.1f, y=%.6f, y*=%.6f  |y-y*|=%.6f" % (float(i) * h, analytical(xs[i]), y[i], math.fabs(y[i] - analytical(xs[i]))))
    if math.fabs(y[i] - analytical(xs[i])) > maxR:
        maxR = math.fabs(y[i] - analytical(xs[i]))

print("||y-y*||=%.6f" % maxR)
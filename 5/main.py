import numpy as np
from numpy import linalg as la

A = 1
B = 5
n = 9
m = 4
h = (B - A) / (n - 1)
y = [0.96, 2.07, 1.96, 2.62, 3.75, 4.12, 3.98, 3.63, 4.70]

x = []
x2 = []
a = []
b = [0] * m

for i in range(n + 1):
    x.append(A + i * h)
    x2.append(A + (i + 1 / 2) * h)

for i in range(m):
    a.append([])
    for j in range(m):
        a[i].append(0)
        for k in range(n):
            a[i][j] += x[k] ** (i + j)

for i in range(m):
    b[i] = 0
    for k in range(n):
        b[i] += y[k] * (x[k] ** i)

for i in range(m):
    b[i] = [b[i]]

print("a: ", a)
print("b: ", b)

M1 = la.inv(a)
lambda_ = np.dot(M1, b)
print("lambda: ", lambda_)

z = []
z2 = []
for k in range(n):
    z_k = 0
    z2_k = 0
    for i in range(m):
        z_k += lambda_[i][0] * x[k] ** i
        z2_k += lambda_[i][0] * x2[k] ** i
    z.append(z_k)
    z2.append(z2_k)

# Calculate absolute error
Delta = 0
for k in range(n):
    Delta += (y[k] - z[k]) ** 2

Delta = (Delta ** (1 / 2)) / (n ** (1 / 2))
print("absolute error:", Delta)

# Calculate relative error
delta = 0
for k in range(n):
    delta += y[k] ** 2
delta = Delta / delta
print("relative error:", delta)

# Print results in a table
print("xt yt rest delta")
for k in range(n):
    print(f"x: {x[k]:.2f} y: {y[k]:.2f} result: {z[k]:.8f} delta: {abs(y[k] - z[k]):.8f}")
    if k != n - 1:
        print(f"x: {x2[k]:.2f} result: {z2[k]:.8f}")

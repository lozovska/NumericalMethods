import math

eps = 0.1

def testFunc(x):
    return math.exp(x)
    #return x ** 2 * math.exp(x-2)

def richardsonFormula(I_h, I_h2, k):
    return (I_h - I_h2) / (2 ** k - 1)

def rect(f, a, b, n):
    h = (b - a) / n
    s = sum(f(a + (i - 0.5) * h) for i in range(1, n + 1))
    return h * s

def trap(f, a, b, n):
    h = (b - a) / n
    s = sum(f(a + i * h) for i in range(1, n))
    return h * ((f(a) + f(b)) / 2 + s)

def Simpson(f, a, b, n):
    h = (b - a) / n
    s1 = sum(f(a + i * h) for i in range(1, n))
    s2 = sum(f(a + (i - 0.5) * h) for i in range (1, n + 1))
    s3 = sum(f(a + (i - 1) * h) for i in range(1, n + 2))
    s = s1 + 4 * s2 + s3
    return h / 6 * s

def res(metd, k, a, b, f):
    n = 1
    R = 100
    iter = 0
    I_h = 0
    while not (abs(R) < eps):
        n *= 2
        I_h2 = I_h
        I_h = metd(f, a, b, n)
        R = richardsonFormula(I_h, I_h2, k)
        iter += 1
    print(f' шаги = {iter}')
    print(f' ответ = {I_h}')
    print(f' ответ + уточнение Ричардсона = {I_h + R}')
    print(f' |I-I*| = {abs(math.e - 1 - I_h - R)}')
    #print(f' |I-I*| = {abs(2 - 5 * math.e ** (-3) - I_h - R)}')

if __name__ == "__main__":
    print("Test Function: exp(x)")
    for i in range(1,4) :
        print("\n----------------------Epsilon = " + str(eps)+ "----------------------")
        print("Метод центральных прямоугольников: ")
        res(rect, 2, 0, 1, testFunc)
        print("Метод трапеций: ")
        res(trap, 2, 0, 1, testFunc)
        print("Метод Симпсона: ")
        res(Simpson, 4, 0, 1, testFunc)
        eps = eps / 10
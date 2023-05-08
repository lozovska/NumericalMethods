from sympy import *

eps = 0.001
x, y = symbols('x y')

def f():
    return x**2 + 4*x*y + 17*y**2 + 5*y

def analytical_min(f, variables):
    # Получаем частные производные функции f по переменным variables
    partial_derivatives = [diff(f, variable) for variable in variables]
    # Решаем систему уравнений, приравнивая частные производные к нулю
    solution = solve(partial_derivatives, variables)
    # Возвращаем координаты минимума
    return tuple(solution[variable] for variable in variables)

print('f: ', f())
fx = diff(f(), x)
fy = diff(f(), y)
print('df/dx: ', fx)
print('df/dy: ', fy)
print('d^2f/dx^2: ',diff(fx, x))
print('d^2f/dxdy: ',diff(fx, y))
print('d^2f/dy^2: ',diff(fy, y))
print()
k = 0
xk, yk = 0.0, 0.0

while(max(abs(fx.subs({x: xk, y: yk})), abs(fy.subs({x: xk, y:yk}))) >= eps):
    phi1 = - (fx.subs({x: xk, y: yk}))**2 - (fy.subs({x: xk, y: yk}))**2
    phi2 = diff(fx, x).subs({x: xk, y: yk}) * (fx.subs({x: xk, y: yk}))**2 + \
           2 * diff(fx , y).subs({x: xk, y: yk}) * fx.subs({x: xk, y: yk}) * fy.subs({x: xk, y: yk}) \
           + diff(fy, y).subs({x: xk, y: yk}) * (fy.subs({x: xk, y: yk}))**2
    t_start = - phi1 / phi2
    xk = xk - t_start * fx.subs({x: xk, y: yk})
    yk = yk - t_start * fy.subs({x: xk, y: yk})
    k +=1

print(f'methods min {xk, yk}')
print(f'analytical min: {analytical_min(f(), [x,y])}')
print(f'delta: {abs(xk -analytical_min(f(), [x,y])[0]), abs(yk -analytical_min(f(), [x,y])[1])}')

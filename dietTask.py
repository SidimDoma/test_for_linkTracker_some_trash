from scipy.optimize import linprog

c = [450, 50, 80, 100]

A = [
    [-250, -20, -30, -10],
    [0, -170, -50, -120],
    [-150, 0, -30, 0],
    [0, 0, -0.5, -0.7],
    [-30, -5, -1, -1]
]

b = [-50, -150, -40, -0.7, -10]

x_bounds = (0, None)
bounds = [x_bounds, x_bounds, x_bounds, x_bounds]

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if res.success:
    print(f"Статус: {res.message}")
    print(f"Оптимальный рацион:")
    print(f" - Говядина: {res.x[0]:.3f} кг")
    print(f" - Картофель: {res.x[1]:.3f} кг")
    print(f" - Молоко: {res.x[2]:.3f} л")
    print(f" - Апельсины: {res.x[3]:.3f} кг")
    print(f"Минимальная стоимость рациона: {res.fun:.2f} руб.")
else:
    print("Решение не найдено.")
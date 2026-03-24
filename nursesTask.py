import numpy as np
from scipy.optimize import linprog

b = np.array([16, 15, 12, 14, 15, 18, 19])

A = np.array([
    [1, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1],
])

c = np.ones(7)

res = linprog(c, A_ub=-A, b_ub=-b, bounds=(0, None), method='highs')

if res.success:
    x = np.ceil(res.x)
    days = ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"]

    print("Количество медсестер, начинающих смену в:")
    for day, val in zip(days, x):
        print(f"{day}: {int(val)}")

    print(f"\nОбщее количество медсестер: {int(sum(x))}")
    print(f"Минимальные затраты: {int(sum(x) * 12000)} руб.")
else:
    print("Решение не найдено")
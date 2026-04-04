import numpy as np
from scipy.optimize import linprog

inputs = np.array([
    [40.2, 2.0, 37], [18.1, 1.1, 17], [42.5, 2.1, 41], [11.0, 0.8, 10],
    [24.8, 1.3, 22], [21.1, 1.3, 19], [13.5, 1.0, 13], [28.6, 1.3, 26],
    [23.5, 1.3, 22], [15.9, 1.0, 15], [23.2, 1.3, 22], [26.0, 1.4, 25],
    [11.1, 0.8, 11], [28.8, 1.6, 26], [19.7, 1.3, 18]
])

outputs = np.array([
    [602], [269], [648], [188], [420], [374], [247], [512],
    [411], [285], [397], [466], [198], [530], [357]
])

n_schools = len(inputs)
n_inputs = inputs.shape[1]
n_outputs = outputs.shape[1]


def solve_dea():
    results = []
    for i in range(n_schools):
        c = np.concatenate([np.zeros(n_inputs), -outputs[i]])
        A_eq = np.zeros((1, n_inputs + n_outputs))
        A_eq[0, :n_inputs] = inputs[i]
        b_eq = [1]

        A_ub = np.hstack([-inputs, outputs])
        b_ub = np.zeros(n_schools)

        res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                      bounds=(1e-6, None), method='highs')

        if res.success:
            results.append(round(-res.fun, 4))
        else:
            results.append(None)
    return results


efficiency_scores = solve_dea()

print("Эффективность школ:")
for idx, score in enumerate(efficiency_scores, 1):
    if score is not None:
        status = "Эффективна" if score >= 0.999 else "Неэффективна"
        print(f"Школа {idx:2}: {score:.4f} ({status})")
    else:
        print(f"Школа {idx:2}: Ошибка оптимизации")
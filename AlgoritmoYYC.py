import random
def find_compatible_set(tau, xp, rows):
    ref_sm = [list(row[i] for i in tau) + [row[xp]] for row in rows]
    
    condition1 = sum(1 for rs in ref_sm if sum(rs) == 1) >= len(tau) + 1
    ref_sm = [rs for rs in ref_sm if sum(rs) == 1]
    condition2 = all(sum(xk) >= 1 for xk in zip(*ref_sm))

    return condition1 and condition2

def yyc_algorithm(basic_matrix):
    psi_star = set()

    r1 = basic_matrix[0]
    for xj in range(len(r1)):
        if r1[xj] == 1:
            psi_star.add((xj,))

    for ri in basic_matrix[1:]:
        psi_aux = set()

        for tau_j in psi_star:
            xp_set = [xp for xp, value in enumerate(ri) if value == 1]

            if any(ri[xp] == 1 for xp in tau_j):
                psi_aux.add(tau_j)
            else:
                for xp in xp_set:
                    if find_compatible_set(tau_j, xp, basic_matrix):
                        psi_aux.add(tau_j + (xp,))

        psi_star = psi_aux

    # Remove duplicates and sort the testors
    psi_star = sorted(set(psi_star))

    return psi_star


def generate_random_matrix(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

# Generar matriz aleatoria 5x5
matrix_5x5 = generate_random_matrix(5, 5)
print("Matriz Aleatoria 5x5:")
for row in matrix_5x5:
    print(row)

result = yyc_algorithm(matrix_5x5)
print("\nConjunto de Testores Típicos:")
for testor in result:
    print(tuple(x+1 for x in testor))
for row in matrix_5x5:
    if all(value == 0 for value in row):
        print("Existe una fila de 0")
        break

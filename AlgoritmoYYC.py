def find_compatible_set(tau, xp):
    for xi in tau:
        if not is_compatible(xi, xp):
            return False
    return True

def is_compatible(xi, xp):
    return True

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
                    if find_compatible_set(tau_j, xp):
                        psi_aux.add(tau_j + (xp,))

        psi_star = psi_aux

    return psi_star

basic_matrix = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 1]
]

result = yyc_algorithm(basic_matrix)
print("Conjunto de Testores Típicos:", result)

import random
import time 
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
                psi_aux.add(tuple(sorted(tau_j)))
            else:
                for xp in xp_set:
                    if find_compatible_set(tau_j, xp, basic_matrix):
                        psi_aux.add(tuple(sorted(tau_j + (xp,))))

        psi_star = psi_aux

    # Ordenar los testores y eliminar repetidos
    psi_star = sorted(set(psi_star))

    return psi_star


def generate_random_matrix(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

while True:
    print("\n1. Generar una matriz aleatoria")
    print("2. Ingresar una matriz personalizada")
    print("3. Salir")
    choice = input("Elige una opción: ")

    if choice == '1':
        # Generar matriz aleatoria 5x5
        matrix = generate_random_matrix(5, 5)
        print("\nMatriz generada:")
        for row in matrix:
            print(row)
    elif choice == '2':
        print("Ingresa la matriz (una fila a la vez, separando los valores por espacio):")
        matrix = []
        while True:
            row_input = input()
            if not row_input:
                break
            row = list(map(int, row_input.split()))
            matrix.append(row)
        print("\nMatriz ingresada:")
        for row in matrix:
             print(row)
    elif choice == '3':
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
        continue

    #tiempo de ejecucion
    start_time = time.time()


    # Calcular los testores típicos
    result = yyc_algorithm(matrix)

    print("\nTiempo de ejecución: %s segundos" % (time.time() - start_time))

    num_testors = len(result)
    print("\nNúmero de Testores Típicos:", num_testors)

    print("\nConjunto de Testores Típicos:")
    for testor in result:
        print(tuple(x+1 for x in testor))

    # Validar si la matriz tiene una fila de 0
    if any(all(value == 0 for value in row) for row in matrix):
        print("La matriz tiene una fila de 0.")
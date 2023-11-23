# Algoritmo-YY
Este código implementa el algoritmo YYC para encontrar testores típicos en una matriz binaria. 

La función `yyc_algorithm(basic_matrix)` es la implementación principal del algoritmo YYC. Toma una matriz binaria como entrada y devuelve un conjunto de testores típicos. Inicialmente, se crea un conjunto vacío `psi_star`. Luego, para cada elemento en la primera fila de la matriz, si el elemento es 1, se añade su índice al conjunto `psi_star`. 

Después de procesar la primera fila, el algoritmo procede a las siguientes filas de la matriz. Para cada fila, se crea un nuevo conjunto `psi_aux`. Luego, para cada testor en `psi_star`, se crea un conjunto `xp_set` que contiene los índices de los elementos que son 1 en la fila actual. Si cualquier elemento en `tau_j` es 1 en la fila actual, se añade `tau_j` a `psi_aux`. De lo contrario, para cada índice en `xp_set`, si el índice es compatible con `tau_j`, se añade una nueva tupla que contiene `tau_j` y el índice a `psi_aux`. Finalmente, `psi_star` se actualiza para ser `psi_aux`.

Después de procesar todas las filas, se eliminan los duplicados de `psi_star` y se ordenan los testores. Finalmente, `psi_star` se devuelve como el resultado del algoritmo.

La función `generate_random_matrix(rows, cols)` genera una matriz aleatoria de tamaño especificado con valores binarios (0 o 1). Utiliza una comprensión de lista para generar las filas y las columnas de la matriz.

El bucle `while True` en la parte inferior del código presenta un menú al usuario para generar una matriz aleatoria, ingresar una matriz personalizada o salir. Dependiendo de la elección del usuario, se genera o se ingresa una matriz, y luego se calculan los testores típicos utilizando la función `yyc_algorithm`.
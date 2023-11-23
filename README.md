# Algoritmo-YYC
Implementación del algoritmo YYC para calcular el conjunto de todos los testores típicos dentro de una matriz

Este código en Python implementa el algoritmo YYC, que se utiliza para encontrar testores típicos en una matriz básica. Un testor es un subconjunto de atributos en un conjunto de datos que es capaz de distinguir entre diferentes clases de datos. Los testores típicos son testores mínimos que no pueden reducirse aún más.

La función yyc_algorithm es la función principal que implementa el algoritmo YYC. Toma como entrada una matriz básica, donde cada fila representa un atributo y cada columna representa un objeto. El valor 1 indica que el atributo se aplica al objeto, y 0 indica lo contrario.

La función comienza inicializando un conjunto vacío llamado psi_star. Este conjunto eventualmente contendrá los testores típicos. Luego, itera sobre la primera fila de la matriz básica, agregando cada atributo que se aplica al primer objeto (es decir, donde el valor es 1) a psi_star como una tupla de un solo elemento.

A continuación, la función itera sobre las filas restantes de la matriz básica. Para cada fila, inicializa un conjunto auxiliar llamado psi_aux. Luego, itera sobre cada testor en psi_star. Para cada testor, crea una lista xp_set de atributos que se aplican al objeto actual. Si algún atributo en el testor se aplica al objeto actual, se agrega el testor a psi_aux. De lo contrario, se verifica cada atributo en xp_set para ver si es compatible con el testor (usando la función find_compatible_set). Si lo es, se agrega un nuevo testor a psi_aux que incluye el atributo.

La función find_compatible_set verifica si un atributo es compatible con un testor. Lo hace iterando sobre cada atributo en el testor y verificando si es compatible con el atributo (usando la función is_compatible). Si algún atributo en el testor no es compatible, devuelve False. De lo contrario, devuelve True.

La función is_compatible es un marcador de posición en este código. Siempre devuelve True, lo que significa que se considera que cualquier atributo es compatible con cualquier testor. En una aplicación del mundo real, esta función contendría la lógica para determinar si un atributo es compatible con un testor según los requisitos específicos del conjunto de datos.

Finalmente, después de iterar sobre todas las filas de la matriz básica, la función devuelve psi_star, que ahora contiene los testores típicos.

El código luego crea una matriz básica, ejecuta el algoritmo YYC en ella e imprime el conjunto resultante de testores típicos. 
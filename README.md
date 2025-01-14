
# Typical Testor Finder

This Python program identifies **Typical Testors** from a given binary matrix. Typical Testors are crucial in feature selection and dimensionality reduction in various fields, such as pattern recognition and data analysis.

---

## Features

- **Generate Random Matrix:** Automatically create a random binary matrix.
- **Custom Matrix Input:** Manually input your binary matrix for analysis.
- **Typical Testor Calculation:** Efficiently calculate and display the set of typical testors.
- **Execution Time Tracking:** Measure and display the time taken to compute the testors.
- **Validation for Zero Rows:** Check if the matrix contains any rows filled entirely with zeros.

---

## How to Use

1. **Run the Script**: Execute the script in your Python environment.
2. **Choose an Option**:
   - `1`: Generate a random 5x5 binary matrix.
   - `2`: Input a custom binary matrix.
   - `3`: Exit the program.
3. **View Results**:
   - The script displays the generated or input matrix.
   - Typical Testors are calculated and displayed.
   - Execution time is provided for performance analysis.

---

## Example Usage

### Menu

```
1. Generar una matriz aleatoria
2. Ingresar una matriz personalizada
3. Salir
Elige una opción: 
```

### Random Matrix Example

1. Select option `1`.
2. A random 5x5 binary matrix is generated:

```
Matriz generada:
[0, 1, 1, 0, 1]
[1, 0, 0, 1, 1]
[1, 1, 0, 0, 1]
[0, 1, 1, 1, 0]
[1, 0, 1, 0, 0]
```

3. Typical Testors are calculated:

```
Número de Testores Típicos: 4

Conjunto de Testores Típicos:
(1, 2)
(1, 3)
(2, 4)
(3, 5)
```

4. Execution time is displayed:

```
Tiempo de ejecución: 0.00345 segundos
```

### Custom Matrix Example

1. Select option `2`.
2. Enter a binary matrix row by row, separated by spaces. For example:

```
1 0 1
0 1 0
1 0 0
```

3. Press Enter on an empty line to finish input. The program processes the input and displays results as in the random matrix example.

---

## Requirements

- **Python 3.6 or higher**
- **Standard Libraries**:
  - `random`
  - `time`

---

## Notes

- Ensure that the matrix is binary (values are only `0` or `1`).
- The program includes validation to check for rows with all zeros.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

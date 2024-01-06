def counting_sort(arr: list[int]) -> list[int]:
    # Encontrar el valor máximo en el array
    max_value = max(arr)
    
    # Inicializar arrays para contar, sumas y el array de salida
    count  = [0 for _ in range(max_value+1)]  # Almacena la cantidad de ocurrencias de cada elemento
    sums   = [0 for _ in range(max_value+1)]  # Almacena la suma acumulativa de las ocurrencias
    output = [0 for _ in range(len(arr))]      # Array de salida ordenado

    # Contar las ocurrencias de cada elemento en el array de entrada
    for i in arr:
        count[i] += 1
        
    # Calcular las sumas acumulativas de las ocurrencias
    for i in range(1, max_value+1):
        sums[i] = sums[i-1] + count[i-1]
        
    # Colocar cada elemento en su posición correcta en el array de salida
    for i in arr:
        output[sums[i]] = i
        sums[i] += 1
    
    # Devolver el array de salida ordenado
    return output

def main():
    # Ejemplo 1
    arr1 = [2, 4, 4, 4, 1, 0, 0, 2]
    result1 = counting_sort(arr1)
    print(f"Ejemplo 1: {arr1} -> {result1}")

    # Ejemplo 2
    arr2 = [5, 3, 1, 2, 4]
    result2 = counting_sort(arr2)
    print(f"Ejemplo 2: {arr2} -> {result2}")

    # Ejemplo 3 con elementos repetidos
    arr3 = [1, 1, 1, 1, 1]
    result3 = counting_sort(arr3)
    print(f"Ejemplo 3: {arr3} -> {result3}")

if __name__ == "__main__":
    main()
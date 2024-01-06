def counting_sort(arr: list[int]):
    max_value = max(arr)
    count  = [0 for _ in range(max_value+1)]
    sums   = [0 for _ in range(max_value+1)]
    output = [0 for _ in range(len(arr))]

    # Cuento apariciones 
    for i in arr:
        count[i] += 1
        
    for i in range(1, max_value+1):
        sums[i] = sums[i-1] + count[i-1]
        
    for i in arr:
        output[sums[i]] = i
        sums[i] += 1
    return output

arr = [2, 4, 4, 4, 1, 0, 0, 2]
print(counting_sort(arr))
def max_min_select(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        if arr[0] > arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    # Divisão
    mid = len(arr) // 2
    left_max, left_min = max_min_select(arr[:mid])
    right_max, right_min = max_min_select(arr[mid:])

    # Conquista
    overall_max = max(left_max, right_max)
    overall_min = min(left_min, right_min)

    return overall_max, overall_min

# Teste
if __name__ == "__main__":
    seq = [3, 5, 1, 9, 2, 8, -1, 7]
    maximum, minimum = max_min_select(seq)
    print(f"Máximo: {maximum}, Mínimo: {minimum}")

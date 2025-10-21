# 10, 3, 3


def integer_partition_of_n_with_len_k(n: int, k: int, num_int):
    """
    Returns the number of ways to partition n into exactly k parts.
    """

    inicial_array = [1 for i in range(k - 1)]
    inicial_array.insert(0, n - (k - 1))
    solution_array = []
    solution_array.append(inicial_array)

    previous_array_index = 0
    while True:
        previous_array = solution_array[previous_array_index][:]
        current_array = solution_array[previous_array_index][:]

        index = 0

        for index in range(k - 1):
            if current_array[index] == previous_array[index]:
                current_array[index] -= 1
                current_array[index + 1] += 1
                break
            if previous_array[index] - current_array[index] == 1:
                continue

        solution_array.append(current_array)

        if previous_array == current_array:
            break

        previous_array_index += 1

    return 1


if __name__ == "__main__":
    print(integer_partition_of_n_with_len_k(10, 3, 3))

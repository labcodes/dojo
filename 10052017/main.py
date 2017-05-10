def collatz(num):

    if num == 1:
        return [1]
    elif num % 2 == 0:
        return [num] + collatz(num / 2)
    else:
        return [num] + collatz((num * 3) + 1)


def maior_caminho(num_list):
    collatz_size_list = []
    for num in num_list:
        collatz_size_list.append(len(collatz(num)))

    max_collatz_size = max(collatz_size_list)
    index_max_collatz_size = collatz_size_list.index(max_collatz_size)

    return num_list[index_max_collatz_size]

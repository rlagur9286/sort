# 시간 복잡도 O(N^2)
# 공간 복잡도 O(N) + 1


def do_selection_sort(input_list):
    for i in range(len(input_list) - 1):
        idx_min = i
        j = i + 1

        while j < len(input_list):
            if input_list[idx_min] > input_list[j]:
                idx_min = j
            j += 1

        if i != idx_min:
            input_list[i], input_list[idx_min] = input_list[idx_min], input_list[i]

    return input_list


if __name__ == '__main__':
    result = do_selection_sort(input_list=[1, 2, 8, 3, 4, 5, 3, 6])
    print(result)
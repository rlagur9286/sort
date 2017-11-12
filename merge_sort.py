# 시간 복잡도 O(n*logn)


def merge_sort(input_list):
    if len(input_list) > 1:
        mid = len(input_list) // 2
        left_list = input_list[:mid]
        right_list = input_list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                input_list[k] = left_list[i]
                i += 1
            else:
                input_list[k] = right_list[j]
                j += 1
            k += 1

        while i < len(left_list):
            input_list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            input_list[k] = right_list[j]
            j += 1
            k += 1

        print('MERGE LISt : ', input_list)

if __name__ == '__main__':
    input_list = [1, 3, 2, 5, 4, 6, 8, 7]
    merge_sort(input_list)
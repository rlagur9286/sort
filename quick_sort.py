def quick_sort(input_list, start, end):
    if start < end:
        pivot = partition(input_list, start, end)
        quick_sort(input_list, start, pivot-1)
        quick_sort(input_list, pivot+1, end)

    return input_list


def partition(input_list, start, end):
    pivot = end
    wall = start
    left = start

    while left < pivot:
        if input_list[left] < input_list[pivot]:
            input_list[left], input_list[wall] = input_list[wall], input_list[left]
            wall += 1
        left += 1
    input_list[pivot], input_list[wall] = input_list[wall], input_list[pivot]
    pivot = wall

    return pivot

if __name__ == '__main__':
    input = [1, 4, 3, 5, 10, 2, 3]
    print(quick_sort(input_list=input, start=0, end=len(input)-1))
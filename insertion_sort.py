def do_insertion_sort(input_list):
    for i, val_num in enumerate(input_list):
        hole_num = i
        while hole_num > 0 and input_list[hole_num - 1] > input_list[hole_num]:
            print(hole_num, input_list[hole_num], input_list[hole_num-1], val_num)
            input_list[hole_num], input_list[hole_num - 1] = input_list[hole_num - 1], input_list[hole_num]
            hole_num -= 1
    return input_list

if __name__ == '__main__':
    result = do_insertion_sort(input_list=[4, 6, 1, 3, 5, 2])
    print(result)
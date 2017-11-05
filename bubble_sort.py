def do_bubble_sort(input_list):
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

    return input_list

if __name__ == '__main__':
    lists = [3, 1, 5, 2, 6 ,2]
    result = do_bubble_sort(lists)
    print(result)
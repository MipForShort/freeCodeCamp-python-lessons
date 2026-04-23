def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = [x for x in array[1:] if x < pivot]
    right = [x for x in array[1:] if x >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)



if __name__ == '__main__':
    print('Empty list:')
    print(quick_sort([]))

    print(quick_sort([20, 3, 14, 1, 5]))

def selection_sort(array):
    if len(array) <= 1:
        return array

    n = len(array)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            temp = array[i]
            array[i] = array[min_index]
            array[min_index] = temp
    return array

if __name__ == '__main__':
    print(selection_sort([33, 1, 89, 2, 67, 245]))
arr = [1, 3, 9, 11, 2, 22, 7]
def bubbleSort(arr):
    for i in range(len(arr)):
        is_sorted = False
        for j in range(len(arr) - 1 -  i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_sorted = True
        if is_sorted == False:
                break
    return(arr)



def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return(arr)

def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr


def merge(left, right):
    output = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])

    return output
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]
    left_partition = merge_sort(left_arr)
    right_partition = merge_sort(right_arr)
    return merge(left_partition, right_partition)


print(merge_sort(arr))
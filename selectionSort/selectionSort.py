from time import clock

# Selection Sort Algorithm

def selectionSort(arr):
    for i in range(0, len(arr)):
        tar = i
        for j in range(i+1, len(arr)):
            if arr[tar] > arr[j]:
                tar = j
        arr[i], arr[tar] = arr[tar], arr[i]
    return arr


if __name__ == "__main__":
    lst = [34, 56, 87, 54, 90, 43, 21, 32, 89]
    start = clock()
    arr = selectionSort(lst)
    print(arr)
    end = clock()
    print((end - start) / 1000)

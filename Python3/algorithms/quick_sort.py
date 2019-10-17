def partition(arr: list, low: int, high: int) -> int:
    divider = low - 1
    pivot = high
    for search in range(low, high):
        if arr[search] <= arr[pivot]:
            divider += 1
            arr[divider], arr[search] = arr[search], arr[divider]
    divider += 1
    arr[divider], arr[pivot] = arr[pivot], arr[divider]
    return divider


def quick_sort(arr: list, low: int, high: int):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
    return


a = [1, 34, 23, 1445, 4, 12, 33, -11, 3, 11, 555, 1000, -1212]
quick_sort(a, 0, len(a) - 1)
print(a)

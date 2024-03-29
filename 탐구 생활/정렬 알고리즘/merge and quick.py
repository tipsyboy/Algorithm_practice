def merge_sort(arr: list) -> None:
    def merge(start: int, end: int) -> None:
        mid = (start + end) // 2
        left, right = start, mid

        for i in range(start, end):
            if right == end:
                temp[i] = arr[left]
                left += 1
            elif left == mid:
                temp[i] = arr[right]
                right += 1
            elif arr[left] <= arr[right]:
                temp[i] = arr[left]
                left += 1
            else:
                temp[i] = arr[right]
                right += 1

        for i in range(start, end):
            arr[i] = temp[i]

    def msort(start: int, end: int) -> None:
        if start + 1 == end:
            return

        mid = (start + end) // 2

        msort(start, mid)
        msort(mid, end)
        merge(start, end)

    temp = [0] * len(arr)
    msort(0, len(arr))


def quick_sort(arr: list) -> None:
    def partition(start: int, end: int) -> int:
        pivot = arr[start]
        left, right = start + 1, end - 1

        while True:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] >= pivot:
                right -= 1

            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]

        arr[start], arr[right] = arr[right], arr[start]

        return right

    def qsort(start: int, end: int) -> None:
        if end - start <= 1:
            return

        pivot = partition(start, end)
        qsort(start, pivot)
        qsort(pivot + 1, end)

    qsort(0, len(arr))


# merge sort
test_arr = [6, -8, 1, 12, 8, 15, 7, -7]
print("og:", test_arr)
merge_sort(test_arr)
print("sorting:", test_arr)

# quick sort
test_arr2 = [6, -8, 1, 12, 8, 3, 7, -7]
print("og:", test_arr2)
quick_sort(test_arr2)
print("sorting:", test_arr2)

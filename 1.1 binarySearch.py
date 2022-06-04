arr = [1,4,5,6,8,9,23,67,554,999]
item = 4
def binarySearch(arr, item):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        print(mid)
        if item == arr[mid]:
            return mid
        if arr[mid] < item :
            low = mid +1
        else:
            high = mid -1
    return None

print(binarySearch(arr, item))
def find(arr, t):
    l, r = 0, len(arr)-1
    while l < r:
        print(l, r)
        mid = (l+r)//2
        if arr[mid] < t:
            l = mid+1
        else:
            r = mid
    return r


print(find([1, 2, 5, 6, 12, 45], 12))

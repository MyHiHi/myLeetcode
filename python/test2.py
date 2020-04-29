class MountainArray():
    def __init__(self, data):
        self.arr, self.size = data, len(data)

    def get(self, i):
        return self.arr[i]

    def length(self):
        return self.size


def findInMountainArray(target, mountain_arr):
    size = mountain_arr.length()
    l, r = 0, size-1
    while (l < r):
        mid = (l + r) >> 1
        if (mountain_arr.get(mid) < mountain_arr.get(mid + 1)):
            l = mid + 1
        else:
            r = mid
        print('l,r', l, r)
    top_index = l
    print('top: ', top_index)
    l, r = 0, top_index
    while l < r:
        mid = (l+r) >> 1
        t = mountain_arr.get(mid)
        print('left: ', mid, t, l, r)
        if (t == target):
            return mid
        elif (t > target):
            r = mid-1
        else:
            l = mid+1
    l, r = top_index, size-1
    while l <= r:
        mid = (l+r) >> 1
        t = mountain_arr.get(mid)
        if t == target:
            return mid
        elif t > target:
            l = mid+1
        else:
            r = mid-1
    return -1


mountain_arr = MountainArray([1, 5, 2])
print(findInMountainArray(2, mountain_arr))

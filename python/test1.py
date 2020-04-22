def subArray(nums, k):
    cnt, sum = 0, 0
    mp = {0: 1}
    for i in nums:
        sum += i
        print("sum: ", sum)
        if mp.get(sum-k):
            print("cnt: ", mp.get(sum-k))
            cnt += mp.get(sum-k)
        mp[sum] = mp.get(sum, 0)+1
        print("mp: ", mp)
    return cnt


print(subArray([1, 1, -1, 1], 2))

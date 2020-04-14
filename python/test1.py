
# def mul(num1, num2):
#     temp = [i*num1 for i in num2]
#     print(temp)
#     res = ''
#     i = 1
#     number = temp[0]
#     while i < len(temp):
#         res += str(number % 10)
#         number //= 10
#         number += temp[i]
#         i += 1
#     # res += str(number)[::-1]
#     # return res[::-1]
#     res = str(number)+res
#     return res


# if __name__ == '__main__':
#     num1 = int(input())
#     str2 = [int(i) for i in input()][::-1]
#     print(mul(num1, str2))
def strMulti(s1, s2):
    n1 = int(s1)
    t = [int(i)*n1 for i in s2[::-1]]
    print(t)
    member, ans, i = t[0], '', 1
    while i < len(t):
        ans = str(member % 10)+ans
        member //= 10
        member += t[i]
        i += 1
    ans = str(member)+ans
    return ans


s1, s2 = input(), input()
print(strMulti(s1, s2))

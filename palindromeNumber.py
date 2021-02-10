# def palindromeNumber(n:int):
#     if n < 0:
#         return False
#
#     s = str(n)
#     palindrom = ''
#     for i in range(len(s)):
#         len1 = len(getLongestPalindrom(s, i, i))
#         if len1 > len(palindrom):
#             palindrom = getLongestPalindrom(s, i, i)
#
#         len2 = len(getLongestPalindrom(s, i, i + 1))
#         if len2 > len(palindrom):
#             palindrom = getLongestPalindrom(s, i, i + 1)
#     if palindrom == s:
#         return True
#     else:
#         return False
#
# def getLongestPalindrom(s, l, r):
#     while l >= 0 and r < len(s) and s[l] == s[r]:
#         l -= 1
#         r += 1
#     return s[l+1 : r]
#
#
# print(palindromeNumber(628826))
#


def isPalindrom(x):
    num = 0
    a = abs(x)
    while(a != 0):
        temp = a % 10
        num = num * 10 + temp
        a = int(a / 10)
        print(num)

    if x >= 0 and x ==num:
        return True
    else:
        return False
print(isPalindrom(121))

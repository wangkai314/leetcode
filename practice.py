class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        palindrom = ''
        for i in range(len(s)):
            len1 = len(self.getLongestPalindrom(s, i, i))
            if len1 > len(palindrom):
                palindrom = self.getLongestPalindrom(s, i, i)

            len2 = len(self.getLongestPalindrom(s, i, i + 1))
            if len2 > len(palindrom):
                palindrom = self.getLongestPalindrom(s, i, i + 1)
        if palindrom == s:
            return True
        else:
            return False

    def getLongestPalindrom(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

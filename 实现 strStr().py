'''
实现 strStr()
'''
class Solution(object):
    def strStr(self, str1, str2):
        '''
        :param str1:  str
        :param str2: str
        :return: int
        '''
        m, n = len(str1), len(str2)
        for index in range(m-n+1):
            if str1[index: index + n] == str2:
                return index
        return -1

if __name__ == '__main__':
    s = Solution()
    str1 = 'leecode'
    str2 = 'code'
    ans = s.strStr(str1, str2)
    print(ans)

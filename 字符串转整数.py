'''
字符串转换整数 (atoi)
'''
class Solution(object):
    def myAtoi(self, str):
        '''
        :param str: str
        :return: int
        '''
        import re
        var = re.match('\s*([+-]?\d+)',str)
        if var is None:
            return 0
        ans = int(var.group())
        return min(max(ans,-2**31),2**31-1)
if __name__ == '__main__':
    s = Solution()
    str = "4193 with words"
    # str = "789 789"
    print(s.myAtoi(str))
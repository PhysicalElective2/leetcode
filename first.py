import math
class Solution:
    def GetUglyNumber_Solution(self, index):
        """
        丑数，只含质因子 2 3 5 的数
        1 是第一个，那么质数都是丑数。直接
        :param index:
        :return:
        """
    def isPrime(self,num):
        """
        质数，好像对解题并没有用
        :param num:
        :return:
        """
        if num<5:
            return num==2 or num==3
        sqrt = num ** 0.5
        for i in range(2,math.ceil(sqrt)+1):
            if(num%i==0):
                return False

        return True

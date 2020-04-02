import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def FirstNotRepeatingChar(self, s):
        """
        在一个字符串(0<=字符串长度<=10000，全部由字母组成)
        中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
        s  是个字符串
        而且返回的应该是位置
        妈的，还可能只出现两次
        其实可以用下面这一句，如果Java还可以lastIndexOf()
        s.count(s[i]) == 1
        :param s:
        :return:
        """
        list=[]# 存字符
        res=[] # 存数量 其实是sum
        resss=[]
        for index,char in enumerate(s):
            if char in list:
                res[list.index(char)]+=1
            else:
                list.append(char)
                res.append(1)
                resss.append(index)
        #遍历数组
        for index,num in enumerate(res):
            if num ==1:
                return resss[index]
        return -1

    def HasSubtree(self, pRoot1, pRoot2):
        #遍历这棵树，找到相同的节点，然后一块继续遍历这棵树
        res=False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                res=self.isSame(pRoot1,pRoot2)
            #以下看着繁琐，其实实现了剪枝
            if not res:
                res=self.isSame(pRoot1.left,pRoot2)
            if not res:
                res=self.isSame(pRoot1.right,pRoot2)
            return res




    def isSame(self,pRoot1,pRoot2):
        """
        判断两棵树是不是相等,这里不要求是相等的，题目要求的是子结构，哎
        :param pRoot1:
        :param pRoot2:
        :return:
        """
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        #还得判断这个值是不是相等呢,这个参考代码真的很漂亮
        return pRoot1.val == pRoot2.val and self.isSame(pRoot1.left, pRoot2.left) and self.isSame(pRoot1.right, pRoot2.right)


    def GetUglyNumber_Solution2(self,index):
        """
        other perfact way
        :param index:
        :return:
        """
        if index  <= 0:
            return 0
        resList=[1]
        p1=0
        p2=0
        p3=0
        for i in range(index-1):#已经有1 在res 中了，只用加index-1 次
            newUgly=min(resList[p1]*2,resList[p2]*3,resList[p3]*5)
            resList.append(newUgly)
            if newUgly%2==0:
                p1+=1
            if newUgly%3==0:
                p2+=1
            if newUgly%5==0:
                p3+=1
        return resList[-1]

    def GetUglyNumber_Solution(self, index):
        """
        丑数，只含质因子 2 3 5         的数,哎，说我的时间太长了
        1
        是第一个，那么质数都是丑数。直接
        :param
        index:
        :return:
        """
        count=1
        start=1
        while(count<=index):
            if self.isUgly(start):
                count+=1
            start+=1
        return start-1

    def isUgly(self, num):
        """
        判断是不是丑数
        :param num:
        :return:
        """
        if num<=6:
            return True
        list=[2,3,5]
        while(True):
            num1=num
            for item in list:
                if(num1%item==0):
                    num1/=item
            if num1==num and num!=1:
                return False
            if num1==1:
                return True
            num=num1

        # while not isPrime(num):
        #     "如果不是质数，还要继续分解"
        #     for i in range(2,math.floor(math.sqrt(num))):
        #         if num%i==0:
        #             #如果i不是235 就不是丑数了
        #             num=num/i
        #             break
        # if
        def isPrime(self, num):
            """
            质数，好像对解题并没有用
            :param num:
            :return:
            """
            if num < 5:
                return num == 2 or num == 3
            sqrt = num ** 0.5
            for i in range(2, math.ceil(sqrt) + 1):
                if (num % i == 0):
                    return False

            return True

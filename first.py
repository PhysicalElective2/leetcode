import math
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def Print3(self, pRoot):
        """
        之字型打印,怎么就是不对呢，郁闷
        真的不想用牛客网了
        也没说明白，其实是要求返回二维数组
        :param pRoot:
        :return:
        """
        res=[]
        if not pRoot:
            return res
        temp=[pRoot]
        flag=True
        while temp:
            size=len(temp)
            row=[]
            if flag:
                for i in range(size):
                    row.append(temp[i].val)
            else:
                for i in range(size):
                    row.append(temp[size - i - 1].val)
            res.append(row)
            flag=not flag
            for i in range(size):
                node=temp.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
        return res

    def Print2(self,pRoot):
        """
        还是别人的办法好啊。。。
        :param pRoot:
        :return:
        """
        res=[]
        if not pRoot:
            return res
        temp=[pRoot]
        while temp:
            size=len(temp)
            row=[]
            for i in temp:
                row.append(i.val)
            res.append(row)
            for i in range(size):
                node=temp.pop(0)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
        return res

    def Print(self, pRoot):
        """
        从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
        请检查是否存在语法错误或者数组越界非法访问等情况
        难以理解我哪里错了
        不过通过这个题目，也感觉到了自己思维的局限性，可以不通过队列实现二叉树的层次遍历
        :param pRoot:
        :return:
        """
        if not pRoot:
            return [[]]
        q = queue.Queue()
        deep = []
        q.put(pRoot)
        deep.append(1)
        res=[]
        while(not q.empty()):
            temp=q.get()
            res.append(temp)
            if temp.left:
                q.put(temp.left)
                deep.append(deep[res.index(temp)]+1)
            if temp.right:
                q.put(temp.right)
                deep.append(deep[res.index(temp)] + 1)
        i=0
        res2=[] #二维数组
        res1=[]
        while i < len(res):
            res1.append(res[i].val)
            if i+1<len(res) and deep[i]!=deep[i+1]:
                res2.append(res1)
                res1=[]
            i+=1
        #一维数组还没遇到终点，就结束了
        if len(res1)>0:
            res2.append(res1)
        return res2




    def isSymmetrical(self, pRoot):
        """
        遍历，判断每一个节点的左右子树,不要求递归对称,这个算法可以剪枝
        :param pRoot:
        :return:
        """

        def is_same(p1, p2):
            if not p1 and not p2:
                return True
            if not p1 and p2:
                return False
            if not p2 and p1:
                return False
            # 这里可以实现剪枝，不用，截断了直接
            return p1.val == p2.val and is_same(p1.left, p2.right) and is_same(p1.right, p2.left)

        if not pRoot:
            return True
        return is_same(pRoot.left, pRoot.right)

    def In_order_traversal(self, p):
        if p.left:
            self.In_order_traversal(p.left)

    def GetNext(self, pNode):
        """
        In-order traversal
        must get the rootnode first

        :param pNode:
        :return:
        """
        if not pNode:
            return pNode
        if pNode.right:
            left1 = pNode.right
            while left1.left:
                left1 = left1.left
            return left1
        while pNode.next:
            temp = pNode.next
            if temp.left == pNode:
                return temp
            pNode = temp
        return None

    def __init__(self):
        # 也可以用两个数组
        self.chr = []
        self.count = []

    def FirstAppearingOnce(self):
        for i, item in enumerate(self.count):
            if item == 1:
                return self.chr[i]
        return '#'

    def Insert(self, char):
        hava = False
        for i, item in enumerate(self.chr):
            if item == char:
                self.count[i] += 1
                hava = True
        if not hava:
            self.chr.append(char)
            self.count.append(1)

    def match(self, s, pattern):
        """
        字符串匹配
        模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）
        思想有问题，这就不可能通过
        有些测试案例就有问题，以后在做。。。。
        "aa"
        "a*"
        :param s:
        :param pattern:
        :return:
        """
        if s == pattern:
            return True
        i = 0
        j = 0
        while i < len(s) and j < len(pattern):
            if s[i] == pattern[j] or pattern[j] == '.':
                i += 1
                j += 1
            elif j + 1 < len(pattern) and pattern[j + 1] == '*':  # 这里会数组越界
                while s[i] == pattern[j]:
                    i += 1
                j += 2
            else:
                return False
        # 没有处理完,还剩b*
        if j != len(pattern) and pattern[j + 1] == '*':
            return True
        return i == len(s) and j == len(pattern)

    def multiply(self, A):
        B = []
        for i in A:
            B.append(1)
        for i, item in enumerate(B):
            for j, jtem in enumerate(A):
                if i != j:
                    B[i] *= A[j]
        return B

    def IsContinuous(self, numbers):
        """扑克牌顺子
        如果没有0
        如果有重复 false
        如果
        """
        """这个意义确实不大啊"""
        if not numbers:
            return False
        if 0 not in numbers:
            return len(numbers) == len(set(numbers)) and max(numbers) - min(numbers) == 4
        else:
            # 有大小王
            kingNum = 0
            for item in numbers:
                if item == 0:
                    kingNum += 1
            numbers.sort()
            return len(numbers[kingNum:]) == len(set(numbers[kingNum:])) and max(numbers[kingNum:]) - min(
                numbers[kingNum:]) <= 4

    def FindContinuousSequence5(self, tsum):
        # write code here,不存储temp sum 的双指针，实在是搞不明白自己哪里不对了啊
        if not tsum:
            return []
        p1, p2 = 1, 2
        res = []
        while p1 < p2:
            cur = (p1 + p2) * (p2 - p1 + 1) // 2
            if cur == tsum:
                arr = []
                for item in range(p1, p2 + 1):
                    arr.append(item)
                res.append(arr)
                p2 += 1
            elif cur < tsum:
                p2 += 1
            else:
                p1 += 1
        return res

    def FindContinuousSequence4(self, tsum):
        # 暴力破解
        if tsum < 3:
            return []
        s = []
        for i in range(1, tsum):
            tems = 0
            j = i
            while tems < tsum:
                tems += j
                j += 1

            if tems == tsum:
                s.append(range(i, j))
        return s

    def FindContinuousSequence3(self, tsum):
        # 存储temp sum 的双指针
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1) / 2
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big + 1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output

    def FindContinuousSequence2(self, tsum):
        """
        上一个就是不行啊，无奈，我明明用了200个测试用例都可以
        :param tsum:
        :return:
        """
        res = []
        if tsum < 0:
            return res
        n = 2
        while (n * n + 1 <= 2 * tsum):
            x0 = (2 * tsum + n - n ** 2) / (2 * n)
            if math.floor(x0) == x0:
                x0 = math.floor(x0)
                # 那么这个就是要的答案
                res.append(range(x0, x0 + n))
            n += 1
        res2 = []
        for item in range(len(res)):
            res2.append(res.pop())
        return res2

    def FindContinuousSequence(self, tsum):
        """
        和 为s 的连续正序列
        :param tsum:
        :return:
        """
        # first ,get  the biggest n
        max_n = 2 * tsum ** 0.5
        res = []
        for i in range(2, math.floor(max_n) + 1):

            tempres = []
            tempsum = i * (i + 1) / 2
            for ii in range(math.ceil(tsum / i)):
                if tempsum + ii * i == tsum:

                    for iii in range(i):
                        tempres.append(ii + iii + 1)
                    res.append(tempres)

        res2 = []
        for item in range(len(res)):
            res2.append(res.pop())
        return res2

    def depth(self, pRoot):
        """
        get the depth
        :param pRoot:
        :return:
        """
        if not pRoot:
            return 0
        return max(self.depth(pRoot.left), self.depth(pRoot.right)) + 1

    def IsBalanced_Solution2(self, pRoot):
        if not pRoot:
            return True
        if abs(self.depth(pRoot.left) - self.depth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution2(pRoot.left) and self.IsBalanced_Solution2(pRoot.right)

    depths = []

    def dfs(self, pRoot, depth):
        if not pRoot:
            # this is leaf node
            self.depths.append(depth)
            return
        self.dfs(pRoot.left, depth + 1)
        self.dfs(pRoot.right, depth + 1)

    def IsBalanced_Solution(self, pRoot):
        """
        解决问题的思想就有问题，平衡二叉树会出现，叶子节点层次数差大于二，但是依然是平衡二叉树
        determine if a tree is an equilibrium binary tree
        need dfs
        :param pRoot:
        :return:
        """
        self.dfs(pRoot, 0)
        # determine the list of depth
        min_ = self.depths[0]
        max_ = self.depths[0]
        for item in self.depths:
            print(item)
            min_ = min(min_, item)
            max_ = max(max_, item)
        if max_ - min_ >= 2:
            return False
        else:
            return True

    def bigger(self, num, list):
        print(list)
        count = 0
        for item in list:
            if item > num:
                count += 1
        return count

    def InversePairs(self, data):
        """
        逆序对,这个方法，时间复杂度过高
        :param data:
        :return:
        """
        res = []
        for i, item in enumerate(data):
            # 遍历
            # 查找这个数之前，比这个数目大的,不行过滤器返回
            res.append(self.bigger(item, data[0:i]))
        return sum(res) % 1000000007

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
        list = []  # 存字符
        res = []  # 存数量 其实是sum
        resss = []
        for index, char in enumerate(s):
            if char in list:
                res[list.index(char)] += 1
            else:
                list.append(char)
                res.append(1)
                resss.append(index)
        # 遍历数组
        for index, num in enumerate(res):
            if num == 1:
                return resss[index]
        return -1

    def HasSubtree(self, pRoot1, pRoot2):
        # 遍历这棵树，找到相同的节点，然后一块继续遍历这棵树
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.isSame(pRoot1, pRoot2)
            # 以下看着繁琐，其实实现了剪枝
            if not res:
                res = self.isSame(pRoot1.left, pRoot2)
            if not res:
                res = self.isSame(pRoot1.right, pRoot2)
            return res

    def isSame(self, pRoot1, pRoot2):
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
        # 还得判断这个值是不是相等呢,这个参考代码真的很漂亮
        return pRoot1.val == pRoot2.val and self.isSame(pRoot1.left, pRoot2.left) and self.isSame(pRoot1.right,
                                                                                                  pRoot2.right)

    def GetUglyNumber_Solution2(self, index):
        """
        other perfact way
        :param index:
        :return:
        """
        if index <= 0:
            return 0
        resList = [1]
        p1 = 0
        p2 = 0
        p3 = 0
        for i in range(index - 1):  # 已经有1 在res 中了，只用加index-1 次
            newUgly = min(resList[p1] * 2, resList[p2] * 3, resList[p3] * 5)
            resList.append(newUgly)
            if newUgly % 2 == 0:
                p1 += 1
            if newUgly % 3 == 0:
                p2 += 1
            if newUgly % 5 == 0:
                p3 += 1
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
        count = 1
        start = 1
        while (count <= index):
            if self.isUgly(start):
                count += 1
            start += 1
        return start - 1

    def isUgly(self, num):
        """
        判断是不是丑数
        :param num:
        :return:
        """
        if num <= 6:
            return True
        list = [2, 3, 5]
        while (True):
            num1 = num
            for item in list:
                if (num1 % item == 0):
                    num1 /= item
            if num1 == num and num != 1:
                return False
            if num1 == 1:
                return True
            num = num1

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

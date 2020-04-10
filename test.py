from first import Solution, TreeNode

if __name__=="__main__":
    s=Solution()
    num=0
    #print(str(num) + " " + str(s.isUgly(num)))
   # print(s.GetUglyNumber_Solution(num))
    #print(s.GetUglyNumber_Solution2(num))


    ss="googgle"
    print(s.FirstNotRepeatingChar(ss))
    print( s.InversePairs([1,2,3,4,5,6,7,0]))
    print("tree")
    print(s.FindContinuousSequence(4))
    for i in range(200):
        print(i)
        print(s.FindContinuousSequence2(i))
        print(s.FindContinuousSequence3(i))
        print(s.FindContinuousSequence4(i))
        print(s.FindContinuousSequence5(i))
    num=[1,2,3]
    print(s.IsContinuous(num))
    print(s.multiply(num))
    print(s.match('as','a.b*'))
    print(s.match('aaa','ab*ac*a'))
    s.Insert('a')
    s.Insert('a')
    s.Insert('c')
    s.Insert('a')
    s.Insert('c')
    s.Insert('c')
    s.Insert('e')
    print(s.FirstAppearingOnce())
    #s.FirstAppearingOnce()
    ##厉害，and 还有这样的用法 ，and he or 都是尽量想少运算
    res = " ddd" and []
    print(res)
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    h = TreeNode(7)
    i = TreeNode(8)
    j = TreeNode(9)
    k = TreeNode(10)
    l = TreeNode(11)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = h
    d.left = i
    d.right = j
    e.left = k
    e.right = l
    print(s.Print(a))

    # for i in range(1,100):
    #     if(s.isUgly(i)):
            #print(str(i) + " " + str(s.isPrime(i)))
           # print(str(i) + " " + str(s.isUgly(i)))

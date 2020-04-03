from first import Solution, TreeNode

if __name__=="__main__":
    print("main")
    s=Solution()
    num=0
    #print(str(num) + " " + str(s.isUgly(num)))
   # print(s.GetUglyNumber_Solution(num))
    #print(s.GetUglyNumber_Solution2(num))
    a=TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    another=TreeNode(3)
    another2=TreeNode(6)
    another3=TreeNode(10)
    another.left=another2
    another.right=another3
    a.left=b
    a.right=c
    b.left=d
    b.right=e
    c.left=f

    print(s.HasSubtree(a,another))
    ss="googgle"
    print(s.FirstNotRepeatingChar(ss))
    print( s.InversePairs([1,2,3,4,5,6,7,0]))

    # for i in range(1,100):
    #     if(s.isUgly(i)):
            #print(str(i) + " " + str(s.isPrime(i)))
           # print(str(i) + " " + str(s.isUgly(i)))

from first import Solution

if __name__=="__main__":
    print("main")
    s=Solution()
    for i in range(1,100):
        if(s.isPrime(i)):
            print(str(i) + " " + str(s.isPrime(i)))

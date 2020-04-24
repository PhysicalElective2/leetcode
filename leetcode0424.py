#刷leetcode 精神一下


class Solution:
    def spread(self,s,start,end):

        while(start>=0 and end<len(s) and s[start]==s[end]):
            start-=1
            end+=1
        return s[start+1:end]


    def longestPalindrome(self, s: str) -> str:
        #最长回文子串
        res=s[:1]

        for i in range(0,len(s)):
            res1=self.spread(s,i,i)
            print("奇数" +res1)
            #问题在这里，这个 不一定符合
            res2=self.spread(s,i,i+1)
            print("偶数" +res2)

            res=max(res,res1,res2,key=len)
        return res




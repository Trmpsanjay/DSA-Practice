# User function Template for Python3

class Solution:
    def leftSmaller(self, a, n):
        ans = []
        stack = []
        for ele in n:
            if len(stack) == 0 :
                ans.append(-1)
                stack.append(ele)
            elif stack[-1] < ele:
                ans.append(stack[-1])
                stack.append(ele)
            else:
                while len(stack) > 0 and stack[-1] >= ele:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
                stack.append(ele)
        return ans
                    
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends
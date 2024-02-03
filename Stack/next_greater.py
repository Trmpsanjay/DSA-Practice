#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        """
        1. create stack
        2. traverse from last
        3. if stack is empty save in ans -1 and push ele to stack
        4.if stack top is greater than element then push element in stack and also in ans
        5. if stack top is less than the element then pop the element untill stackele is greter than ele and oush the ele
        """
        stack  = []
        ans = []
        for i in range(n-1,-1,-1):
            if len(stack) == 0:
                ans.append(-1)
                stack.append(arr[i])
            elif len(stack) > 0 and   stack[-1]>arr[i]:
                ans.append(stack[-1])
                stack.append(arr[i])
            elif len(stack)> 0 and stack[-1] <= arr[i]:
                while len(stack) >0 and stack[-1] <= arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
                stack.append(arr[i])
            else:
                pass
        return ans[::-1]
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends
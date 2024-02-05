#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,heights):
        #code here
        nsr = self.nearest_smaller_right(heights)
        nsl = self.nearest_smaller_left(heights)
        
        diff = []
        for i in range(len(heights)):
            diff.append((nsr[i]-nsl[i])-1)
        max = None
        for i in range(len(heights)):
            area = heights[i]*diff[i]
            if max is None:
                max = area
            elif max < area:
                max = area
        return max
    
    
    
    def nearest_smaller_left(self,heights):
        stack = []
        ans = []
        for i in range(len(heights)):
            if len(stack)==0:
                
                ans.append(-1)
            elif stack[-1]['data'] < heights[i]:
                ans.append(stack[-1]['index'])
                
            else:
                while len(stack) > 0 and stack[-1]['data']>=heights[i]:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1]['index'])
            stack.append({
                    'data' : heights[i],
                    'index' : i
                    }
                )
        return ans
    def nearest_smaller_right(self,heights):
            stack = []
            ans = []
            for i in range(len(heights)-1,-1,-1):
                if len(stack)==0:
                    stack.append({
                        'data' : heights[i],
                        'index' : i
                        }
                    )
                    ans.append(len(heights))
                elif stack[-1]['data'] < heights[i]:
                    ans.append(stack[-1]['index'])
                    stack.append({
                        'data' : heights[i],
                        'index' : i
                        }
                    )
                else:
                    while len(stack) > 0 and stack[-1]['data']>=heights[i]:
                        stack.pop()
                    if len(stack) == 0:
                        ans.append(len(heights))
                    else:
                        ans.append(stack[-1]['index'])
                    stack.append({
                        'data' : heights[i],
                        'index' : i
                        }
                    )
            return ans[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends
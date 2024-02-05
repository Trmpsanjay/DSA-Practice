
class Solution:
    def trappingWater(self, height,n):
        max_l = []
        max_ele = height[0]
        for i in range(len(height)):
            max_ele = max(max_ele,height[i])
            max_l.append(max_ele)
        max_r = []
        max_ele = height[-1]
        for i in range(len(height)-1,-1,-1):
            max_ele = max(max_ele,height[i])
            max_r.append(max_ele)
        max_r = max_r[::-1]
        water_volume = 0
        for i in range(len(height)):
            water_volume+=(min(max_r[i],max_l[i])-height[i])
        return water_volume
        #Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends
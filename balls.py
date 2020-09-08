class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def check(position, m, x):
            count, prev = 1, position[0]
            for i in range(1, len(position)):
                if position[i]-prev >= x:
                    count += 1
                    prev = position[i]
            return count >= m
        
        position.sort()
        left, right = 1, position[-1]-position[0]
        while left <= right:
            mid = left + (right-left)//2
            if not check(position, m, mid):
                right = mid-1
            else:
                left = mid+1
        return right
val=Solution()
n,m=map(int,input().split())
arr=list(map(int,input().split()))
print(val.maxDistance(arr,m))

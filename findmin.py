class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(1,len(nums),1):
           if nums[i]<= nums[i-1]:
             return nums[i]
        return nums[0]

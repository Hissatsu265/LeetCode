class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum=0
        for i in nums:
            sum+=i
        s=0
        e=len(nums)-1
        k=e+1
        while sum>=target:
            if nums[s]>nums[e]:
                sum=sum-nums[e]
                e=e-1
            else:
                sum=sum-nums[s]
                s=s-1
            k=k-1
        return k+1

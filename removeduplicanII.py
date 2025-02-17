class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        a=[]
        a.append(nums[0])
        # j=1
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1] and k<1):
                a.append(nums[i])
                k=k+1
            elif nums[i]!=nums[i-1]:
                a.append(nums[i])
                # j+=1
                k=0
        for i in range( len(a)):
            nums[i]=a[i]
        return len(a)

            

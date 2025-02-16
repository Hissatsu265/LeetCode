class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m=m-1
        n=n-1
        k=m+n+1
        while m>=0 and n >=0:
            if(nums1[m]<nums2[n]):
                nums1[k]=nums2[n]
                n=n-1
            else:
                nums1[k]=nums1[m]
                m=m-1
            k=k-1    
        while n>=0:
            nums1[k] = nums2[n]
            n =n- 1
            k =k- 1
        while m>=0:
            # nums1[k] = nums1[m]
            nums1[k]=nums1[m]
            m =m- 1
            k =k- 1
        return nums1 

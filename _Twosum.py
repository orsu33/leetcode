class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for a in range(0,len(nums)):
            b=target-nums[a]
            if(b in d):
                return[a,d[b]]
            d[nums[a]]=a
    
            

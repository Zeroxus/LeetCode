class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return False
        rlist={}
        for i in range(len(nums)):
            if nums[i] in rlist:
                return [rlist[nums[i]],i]
            else:
                rlist[target-nums[i]]=i
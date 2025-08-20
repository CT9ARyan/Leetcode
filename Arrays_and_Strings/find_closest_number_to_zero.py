class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        closest = nums[0]

        for num in nums:
            if (abs(num) < abs(closest)):
                closest = num
            elif (abs(num) == abs(closest)):
                closest = num if closest < num else closest

        return closest
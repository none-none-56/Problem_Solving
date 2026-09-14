class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        pref = [1] * len(nums)
        suff = [1] * len(nums)
        """
        nums = [1 2 4 6]
        [1 1 1 1]
        pre [1 2 8 48]
        suf [6 1]
        """
        for i in range(1, len(pref)):
            pref[i] = pref[i - 1] * nums[i - 1]
        for i in range(len(suff) - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            result[i] = pref[i] * suff[i]
        
        return result
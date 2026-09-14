from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_count = Counter(nums)
        maximum = 0
        
        nums_starter = set()

        for num in nums:
            if (num - 1) not in nums_count:
                nums_starter.add(num) 
        
        # print(nums_starter)

        for start in nums_starter:
            current = 0
            num = start

            while num in nums_count:
                current += 1
                num += 1
            
            maximum = max(current, maximum)

        return maximum


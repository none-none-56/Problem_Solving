from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_count = dict(Counter(nums))
        print(nums_count)

        counts = {}

        for key, val in nums_count.items():
            if val in counts:
                counts[val].append(key)
            else:
                counts[val] = [key]
        
        print(counts)
        
        result = []

        for key, val in dict(sorted(counts.items())).items():
            val.sort(reverse=True)
            for num in val:
                result += [num] * key
        
        return result
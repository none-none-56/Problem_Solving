class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for index, num in enumerate(nums):
            if num not in nums_dict:
                nums_dict[num] = []
            nums_dict[num].append(index)
        
        for index, num in enumerate(nums):
            remainder = target - num
            print(num, remainder)
            if remainder in nums_dict:
                if remainder == num:
                    if len(nums_dict[num]) > 1:
                        return [nums_dict[num][0], nums_dict[num][1]]
                    else:
                        continue
                return sorted([nums_dict[num][0], nums_dict[remainder][0]])

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}
        for string in strs:
            sorted_str = "".join(sorted(string))

            if sorted_str not in group_anagrams:
                group_anagrams[sorted_str] = []
            group_anagrams[sorted_str].append(string)

        return list(group_anagrams.values())
class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + '#' + string
        # print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []

        i = s.find('#')
        while i != -1:
            # print("len ", s[:i])
            string_len = int(s[:i])
            result.append(s[i + 1 : i + string_len + 1])

            s = s[i + string_len + 1:]
            i = s.find('#')
        
        return result
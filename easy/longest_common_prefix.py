class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ''
        if len(strs) < 2:
            return strs[0]
        prefix_len = 1
        while True:
            assume_prefix = strs[0][0: prefix_len]
            if len(assume_prefix) == 0:
                return common_prefix
            if all([s.startswith(assume_prefix) for s in strs]):
                common_prefix = assume_prefix
                prefix_len += 1
                if prefix_len > len(strs[0]):
                    break
            else:
                break
        return common_prefix

s = Solution()

assert s.longestCommonPrefix(["flower","flow","flight"]) == 'fl'
assert s.longestCommonPrefix(["dog","racecar","car"]) == ''
assert s.longestCommonPrefix(['', '']) == ''
assert s.longestCommonPrefix(["flower","flower","flower","flower"]) == 'flower'

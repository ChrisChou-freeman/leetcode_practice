pair_left = ['(', '{', '[']
pair_right = [')', '}', ']']

pair_map: dict[str, str] = {}

for right in pair_right:
    pair_map[right] = pair_left[pair_right.index(right)]

class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        sl = list(s)
        for s in sl:
            if s in pair_left:
                stack.append(s)
            elif s in pair_right:
                left = pair_map[s]
                if len(stack) == 0:
                    return False
                if stack[-1] == left:
                    stack.pop()
                else:
                    stack.append(s)
        return len(stack) == 0

s = Solution()

assert s.isValid('()') is True
assert s.isValid('()[]{}') is True
assert s.isValid('(]') is False
assert s.isValid(']') is False

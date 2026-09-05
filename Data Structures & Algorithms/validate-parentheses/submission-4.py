class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        dicts ={
            ')':  '(',
            '}':  '{',
           "]" :   '[',
        }
        for char in s:
            if char == '(' or char  == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                value = stack.pop()
                if dicts[char] != value:
                    return False
        return len(stack) == 0

        
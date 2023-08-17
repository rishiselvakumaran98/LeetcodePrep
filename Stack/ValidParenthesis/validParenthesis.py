class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2: 
            return False
        closeParenthesis = {
            ')': '(',
            '}' : '{',
            ']' : '['
        }
        openParenthesis = set(['{', '(', '['])
        stack = []
        for char in s:
            if char in openParenthesis:
                stack.append(char)
            # its a close parenthesis
            elif stack:
                if stack.pop() != closeParenthesis[char]:
                    return False
            else:
                return False

        return not stack
    
    def isValid2(self, s: str) -> bool:
        # Create a HashMap to map the end Parenthesis to start
        # while iterating through the string s if the char is start parenthesis we add it to stack
        # else we try to pop the stack and check if its equal counter match to the end parenthesis it should match to 
        # if not we return false
        # the end condition would be to return if the stack is not empty

        endParent = {'}':'{', ')':'(', ']':'['}
        stack = []
        startParent = set(['(', '[', '{'])
        for char in s:
            if char in startParent:
                stack.append(char)
            elif char in endParent and stack:
                if stack.pop() != endParent[char]:
                    return False
            elif not stack:
                return False
        return not stack
    
print(Solution().isValid2("()"))
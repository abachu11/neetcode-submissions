class Solution:
    def isValid(self, s: str) -> bool:
        # Correct dictionary of matching parentheses
        parentheses = {')': '(', 
                       ']': '[', 
                       '}': '{'}
        
        stack = []
        
        for c in s:
            if c in parentheses:
                # Check if the stack is not empty and if the top of the stack matches the expected opening bracket
                if stack and stack[-1] == parentheses[c]:
                    stack.pop()
                else:
                    print(stack)       # Debugging statement
                    print(parentheses[c])  # Debugging statement
                    print(c)           # Debugging statement
                    return False
            else:
                stack.append(c)
        
        print(stack)  # Debugging statement to check the final state of the stack
        
        # Return True if the stack is empty (all brackets matched), False otherwise
        return not stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]

        stack = []
        res = 0
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                a = int(stack.pop())
                b = int(stack.pop())

                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(b-a)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(b/a)
        return int(stack[0])
                

            
            
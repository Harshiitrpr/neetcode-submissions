class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for s in tokens:
            if s == "+":
                a = operands.pop()
                b = operands.pop()
                operands.append(a + b)
            elif s == "*":
                a = operands.pop()
                b = operands.pop()
                operands.append(a * b)
            elif s == "-":
                a = operands.pop()
                b = operands.pop()
                operands.append(b - a)
            elif s == "/":
                a = operands.pop()
                b = operands.pop()
                operands.append(int(b / a))
            else:
                operands.append(int(s))
        return operands[0]
            
        
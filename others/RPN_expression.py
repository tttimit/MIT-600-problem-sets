class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = Stack()
        for i in tokens:
            if i == '+':
                op1 = stack.pop()
                op2 = stack.pop()
                new_op = op2 + op1
                stack.push(new_op)
            elif i == '-':
                op1 = stack.pop()
                op2 = stack.pop()
                new_op = op2 - op1
                stack.push(new_op)
            elif i == '*':
                op1 = stack.pop()
                op2 = stack.pop()
                new_op = op1 * op2
                stack.push(new_op)
            elif i == '/':
                op1 = stack.pop()
                op2 = stack.pop()
                new_op = op2 / op1
                stack.push(new_op)
            else:
                stack.push(int(i))
            print "now stack is: ", stack.show()
        print "---"
        return stack.pop()
        
class Stack():
    def __init__(self):
        self.myList = []
        
    def push(self, item):
        self.myList.append(item)
        
    def pop(self):
        item = self.myList[-1]
        self.myList = self.myList[:-1]
        return item

    def show(self):
        return self.myList
def test():
    s = Solution()
    L = [5, 3, '+']
    L1 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    L2 = ["2", "1", "+", "3", "*"]
    L3 = ["4", "13", "5", "/", "+"]
    s.evalRPN(L)
    s.evalRPN(L1)
    s.evalRPN(L2)
    s.evalRPN(L3)

test()

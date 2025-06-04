class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                #what element

                b = stack.pop()
                #last number

                a = stack.pop()
                #before the last one

                if token =="+":
                    res = a + b
                elif token =="-":
                    res = a - b
                elif token =="*":
                    res = a * b
                elif token =="/":
                     res = int(a / b)
                     # integer po rusky (celoe chislo) ; =D

                stack.append(res)
                 #result
            else:
                stack.append(int(token))
                #the prime number becomes an int and is written to the stack

        return stack[0]




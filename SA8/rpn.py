from stack import Stack

S=Stack()

def compute_rpn(s):                         #   Compute rpn function
    num=s.split()
    for i in range (len(num)):

        if num[i]=="*":                     #   Check for multiplier operator
            b=S.pop()
            c=S.pop()
            result = c*b
            S.addstack(result)              #   Add result onto stack

        elif num[i] == "/":                 #   Check for devide operator
            b = S.pop()
            c = S.pop()
            result =int( c / b)
            S.addstack(result)


        elif num[i] == "+":
            b = S.pop()
            c = S.pop()
            result = c + b
            S.addstack(result)



        elif num[i] == "-":

            b = S.pop()
            c = S.pop()
            result = c - b
            S.addstack(result)



        else:
            S.addstack(int(num[i]))             #Add numbers into operator

    return (S.stack.pop())                      #return computed values of objects in the stack



print(compute_rpn("5 4 /"))
print(compute_rpn("100 20 - 4 /"))
print(compute_rpn("5 13 1 - 4 / + 4 *"))
print(compute_rpn("1 130 5 * 200 - + 7 * 30 /"))
print(compute_rpn("6 30 4 / 5 -  200 - + 3 * 30 "))
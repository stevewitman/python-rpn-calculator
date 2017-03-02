def is_numeric(str):
    try:
        float(str)
        return True
    except:
        return False

def is_operator(str):
    if str == "+" or str== "-" or str == "*" or str == "/":
        return True
    else:
        return False

def calculate(op):
    if len(stack) > 1:
        if op == '+':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
            return stack[-1]
        elif op == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
            return stack[-1]
        elif op == '*':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
            return stack[-1]
        elif stack[-1] != 0:
            b = stack.pop()
            a = stack.pop()
            stack.append(a / b)
            return stack[-1]
        else:
            return "Error: divide by zero"
    else:
        return "Error: stack underflow"



stack = []
data = 'clear'


while data != 'end':
    if is_numeric(data):
        stack.append(float(data))
    elif is_operator(data):
        print calculate(data)
    elif data == "clear":
        stack = []
        print stack
    elif data == '':
        pass
    else:
        print "Error: invalid input"
    data = raw_input(str(stack) + " >")

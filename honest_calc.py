def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        return True
    else: return False
def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1)  and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):" 
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
oper=['+','-','*','/']

memory = 0

while True:
    print(msg_0)
    calc = input()
    calc = calc.split()
    x = calc[0]
    y = calc[2]
    op = calc[1]
    
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    
    try:
        x = float(x)
        y = float (y)
    except ValueError:
        print(msg_1)
        continue
    if not oper.count(op):
        print(msg_2)
        continue
    
    check(x, y, op)
    
    result = 0
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/' and y != 0:
        result = x / y
    else:
        print(msg_3)
        continue
    print(result)
    
    cancel = 0
    while True:
        print(msg_4)
        answer = input()
        if answer == 'y':
        
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(globals()['msg_'+str(msg_index)])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            break
                    elif answer == 'n':
                        cancel = 1
                        break
                    else:
                        continue
            if cancel == 1:
                break

            memory = result
        else: 
            if answer != 'n':
                continue
        break

    n=0
    while True:
        print(msg_5)
        answer = input()
        if answer == 'y':
            n+=1
        else: 
            if answer != 'n':
                continue
        break
    
    if n == 1:
        continue
    break
        
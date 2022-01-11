def zero(*a):
    if a == null:
        return '0'
    else:
        return f'o{a}'
def one(*a):
    if a:
        b = [1]
        b.append(a)
        return b
    else:
        return '1'
def two(*a):
    if a == null:
        return '2'
    else:
        return
def three(*a):
    if a == null:
        return '3'
    else:
        return
def four(*a):
    if a == null:
        return '4'
    else:
        return
def five(*a):
    if a == null:
        return '5'
    else:
        return
def six(*a):
    if a == null:
        return '6'
    else:
        return
def seven(*a):
    if a == null:
        return '7'
    else:
        return
def eight(*a):
    if a == null:
        return '8'
    else:
        return
def nine(*a):
    if a == null:
        return '9'
    else:
        return

def plus(f):
    return ['+',f]
def minus(f):
    return ['-',f]
def times(f):
    return ['*',f]
def divided_by(f):
    return ['/',f]

def submit(s):
    if s[1][0] == '+':
        return s[0]+s[1][1]
    elif s[1][0] == '-':
        return s[0]-s[1][1]
    elif s[1][0] == '*':
        return s[0]*s[1][1]
    elif s[1][0] == '/':
        return s[0]/s[1][1]

print(one(plus(one())))

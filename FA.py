# state yang memungkinkan angka bernilai -
def state0var(c):
    if ord(c) == 95:
        state = 1
    elif ord(c) == 36:
        state = 1
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 1
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 1
    else:
        state = 2

    return state

def state1var(c):
    if ord(c) == 95:
        state = 1
    elif ord(c) == 36:
        state = 1
    elif ord(c) >= 48 and ord(c) <= 57:
        state = 1
    elif ord(c) >= 65 and ord(c) <= 90:
        state = 1
    elif ord(c) >= 97 and ord(c) <= 122:
        state = 1
    else:
        state = 2

    return state

def state2var(c):
    state = 2

    return state

def isVariable(s):
    state = 0
    for i in range (len(s)):
        if (state == 0):
            state = state0var(s[i])
        if (state == 1):
            state = state1var(s[i])
        if (state == 2):
            state = state2var(s[i])
    if (state == 1):
        return True
    else :
        return False

def statenumber0(c):
    if(ord(c) >= 48 and ord(c) <= 57):
        state = 1
    else :
        state = 2

    return state

def statenumber1(c):
    if(ord(c) >= 48 and ord(c) <= 57):
        state = 1
    else :
        state = 2

    return state

def statenumber2(c):
    state = 2

    return state

def isNumber(s):
    state = 0
    for i in range (len(s)):
        if (state == 0):
            state = statenumber0(s[i])
        if (state == 1):
            state = statenumber1(s[i])
        if (state == 2):
            state = statenumber2(s[i])
    if (state == 1):
        return True
    else :
        return False

def reverseInteger(x:int):
    num = str(x)
    temp = str()

    if num[0] == '-':
        temp += '-'

    for i in range(len(num)-1, -1, -1):
        if num[i] == '-':
            pass
        else:
            temp += num[i]

    return int(temp)

print(reverseInteger(-123))
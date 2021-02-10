def addBinary(a: str, b: str) -> str:
    result = ''
    carry = 0
    val = 0

    for i in range(max(len(a), len(b))):
        val = carry
        if i < len(a):
            val += int(a[-(i + 1)])
        if i < len(b):
            val += int(b[-(i + 1)])
        carry = val // 2
        val = val % 2


        result += str(val)

    if carry:
        result += str(1)

    return result[::-1]

print(addBinary('1','11'))
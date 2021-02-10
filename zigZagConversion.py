# def convert(s, numRows):
#     if numRows == 1 or len(s)<=numRows:
#         return s
#
#     zigzag = ['' for i in range(numRows)]
#
#     row, step = 0, 1
#
#     for j in s:
#         zigzag[row] += j
#
#         if row == 0:
#             step = 1
#         elif row == numRows-1:
#             step = -1
#
#         row += step
#
#     return ''.join(zigzag)
#
# print(convert('PAYPALISHIRING', 4))

def covert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    zigzag = ['' for i in range(numRows)]

    row, step = 0, 1

    for j in s:
        zigzag[row] += j

        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1

        row += step

    return ''.join(zigzag)

print(covert('PAYPALISHIRING', 4))

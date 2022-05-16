def plusMinus(arr):
    # Write your code here
    neg, pos, zr = 0, 0, 0
    for n in arr:
        if n < 0: neg += 1
        elif n > 0: pos += 1
        else: zr += 1
    size = len(arr)
    print(pos/size)
    print(neg/size)
    print(zr/size)
def reverse_number(n):
    if n < 0:
        n = str(n)
        n = n[::-1]
        n = n.replace('-', "")
        n = int(n)
        n = n*(-1)
    else:
        n = str(n)
        n = n[::-1]
    return int(n)

reverse_number(-123)
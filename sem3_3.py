def regres(a,b):
    result = []
    while a != 0:
        result.append(a % b)
        a = a//b
        result.reverse()
    return result
num = 88
razraydnost = 2
print(*regres(num, razraydnost))
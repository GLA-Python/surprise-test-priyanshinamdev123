x = list(map(int,input().split()))
def func(x):
    check = x[1]-x[0]
    for i in range(2,len(x)):
        if abs(x[i]-x[i-1])>check:
            check = abs(x[i]-x[i-1])
        else:
            return False
    return True
print(func(x))

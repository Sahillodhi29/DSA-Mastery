def apowerb(a,b):
    if b == 0:
        return 1
    
    return a*apowerb(a,b-1)

print(apowerb(2,3))
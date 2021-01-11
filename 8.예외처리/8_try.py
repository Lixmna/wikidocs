def f(a,b) :
    try :
        if a and b :
            return (a*b) + (a / b)
        elif a:
            return '불능'
        else :
            return '부정'
    except :
        return '똑 바로 살아라'

print(f(3,0))
print(f(0,0))
print(f(0,3))
print(f('이십',500000000))
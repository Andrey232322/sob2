def krug(a):
    s = 3.14 * a**2
    return s

def triangle(a,b,c):
    # периметр P
    P = a+b+c
    # полупериметр p
    p = P//2
    # площадь
    s = (p*(p-a)*(p-b)*(p-c)) ** (0.5)

    # на то, является ли треугольник прямоугольным
    lis = [a,b,c]
    max_stor = max(lis)
    lis.remove(max_stor)
    c = 0
    for i in lis:
        c += i**2
    if c == max_stor**2:
        print('треугольник прямоуголный')
    else:
        print('треугольник не прямоуголный')
    return s
print(krug(3))
print(triangle(4,5,7))
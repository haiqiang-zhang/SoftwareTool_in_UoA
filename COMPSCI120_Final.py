import math
def algorithm_Q7():
    s = 0
    a = 0
    m = 343
    n = 5
    while True:
        if a == m:
            print(m,n)
            break
        else:
            s = s + 1
            a = m + ((-1)**s)*((m-n)-s)
            print(a,s,(m-n)-s)
def runtime_Q8():
    n = 100000000000000000000000000000000000000
    if n**2+(10*math.log2(n)) > ((n*math.log2(n))+(5*n)):
        print(True)
    else:
        print(False)
    print(n**2+(10*math.log2(n)),((n*math.log2(n))+(5*n)))
def freeresponse_QB():
    a = 0
    b = 0
    c = 1
    n = 50
    step_two = 0
    while True:
        if a < n:
            while a < n:
                a = a + 1
                step_two += 1
        elif a == n:
            step_two += 1
            a = 0
            if b < n:
                c = c*n
                b = b + 1
            elif b == n:
                break
    print(step_two, c)



# algorithm_Q7()
# runtime_Q8()
freeresponse_QB()
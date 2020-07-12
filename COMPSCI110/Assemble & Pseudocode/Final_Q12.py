# value = int(input("input value: "))
# power = int(input("input power: "))
# zero = 0
# count = 0
# part = 0
# sumv = 0
#
# def l1():
#     global power
#     global part
#     global zero
#     global sumv
#     global count
#     global r
#     power -= 1
#     r = power
#     if r == zero:
#         print(sumv)
#         pass
#     r = sumv
#     part = r
#     r = value
#     count = r
#
#
# def main():
#     global power
#     global part
#     global zero
#     global sumv
#     global count
#     global r
#     r = value
#     sumv = r
#     l1()
#     while True:
#         count -= 1
#         r = count
#         if r == zero:
#             l1()
#         r = sumv
#         r = r + part
#         sumv = r
#
#
# main()


def main():
    value = 5
    power = 2
    zero = 0
    count = 0
    part = 0
    sumv = 0
    r = value
    sumv = r
    power -= 1
    r = power
    if r == zero:
        print(sumv)
        return
    r = sumv
    part = r
    r = value
    count = r
    while True:
        count -= 1
        r = count
        if r == zero:
            power -= 1
            r = power
            if r == zero:
                print(sumv)
                return
            r = sumv
            part = r
            r = value
            count = r
        r = sumv
        r = r + part
        sumv = r


main()
# def main():
#     get_number = int(input("input number: "))
#     first = 1
#     second = 1
#     value = 0
#     if get_number <= 2:
#         value = 1
#     else:
#         count = 3
#         while count <= get_number:
#             value = first + first + second
#             first = second
#             second = value
#             count += 1
#     print(value)

def main():
    w = 0
    x = 0
    y = 1
    z = 0
    cache_value = int()
    x = int(input("input X: "))
    while True:
        cache_value = x
        if cache_value == z:
            print(w)
            return
        cache_value = w
        cache_value = cache_value + y
        w = cache_value
        y += 1
        x -= 1








while True:
    main()
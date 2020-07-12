def q10_pseudocode():
    number = int(input("input number: "))
    first = 1
    second = 1
    value = 0
    if number <= 2:
        value = 1
    else:
        count = 3
        while count <= number:
            value = first + first +second
            first = second
            second = value
            count = count + 1
    print(value)

def q11_textbook():
    w = 0
    x = 0
    y = 1
    z = 0
    x = int(input("input x: "))
    while True:
        r = x
        if r == z:
            print(w)
            break
        r = w
        r = r + y
        w = r
        y += 1
        x -= 1



while True:
    # q10_pseudocode()
    q11_textbook()
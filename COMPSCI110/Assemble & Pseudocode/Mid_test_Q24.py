n = int(input("input: "))
term = 1
sum = 0
r_list = []
n_list = []
term_list = []
sum_list = []
while True:
    r = term
    r_list.append(r)
    if n < r:
        print(sum)
        break
    else:
        r = r + sum
        r_list.append(r)
        sum = r
        sum_list.append(sum)
        term += 1
        term_list.append(term)

print(r_list)
print(n_list)
print(term_list)
print(sum_list)
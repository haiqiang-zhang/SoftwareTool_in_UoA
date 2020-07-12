x = int(input())
y = int(input())
r_list = []
r = x
r_list.append(r)
r = r + x
r_list.append(r)
r = r + x
r_list.append(r)
x = r
r = y
r_list.append(r)
r = r + y
r_list.append(r)
y = r
r = x
r_list.append(r)
r = r - y
r_list.append(r)
x = r
print(r_list)
print(x)
print(y)


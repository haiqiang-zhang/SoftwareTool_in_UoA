input1 = 6
input2 = 3
input3 = 5
n = input1
term = input2
diff = input3
sumv = 0
countv = 1
while countv <= n:
    sumv = sumv + term
    countv = countv + 1
    term = term + diff
print(sumv)
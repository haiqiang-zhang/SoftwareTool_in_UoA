'''
for index1 in range(1, 10):
    for index2 in range(1, 10):
        for index3 in range(1, 10):
            for index4 in range(1, 10):
                for index5 in range(1, 10):
                    for index6 in range(1, 10):
                        for index7 in range(1, 10):
                            for index8 in range(1, 10):
                                number_sum_ascii = ord(str(index1))+ord(str(index2))+ord(str(index3))+ord(str(index4))+ord(str(index5))+ord(str(index6))+ord(str(index7))+ord(str(index8))
                                the_pass = str(index1)+str(index2)+str(index3)+str(index4)+str(index5)+str(index6)+str(index7)+str(index8)
                                if number_sum_ascii%11 == 5:
                                    print(the_pass, number_sum_ascii,number_sum_ascii%11)
'''

'''
list_mod = "104,122,104,97,53,53,54,49,50,51,52,53,54,55".split(",")
result_list = []
sum_result = 0
for index in range(len(list_mod)):
    list_mod[index] = int(list_mod[index])
for index in range(len(list_mod)):
    sum_result += list_mod[index]
print(sum_result)
'''


'''
same_hash_list = []
for index in range(65, 91):
    if index % 11 == 5:
        same_hash_list.append(chr(index))
print(same_hash_list)
'''


m = 396
for d in range(0, m+1):
    if (283*d)%m == 1:
        print(d)

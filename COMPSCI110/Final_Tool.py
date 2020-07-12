# password = "fi23do54"
# ascii_sum = 0
# for index in range(len(password)):
#     ascii_sum = ascii_sum + ord(password[index])
# ascii_sum = ascii_sum % 11
# print(ascii_sum)
# ascii_sum = (ascii_sum + 50) * 2
# print(ascii_sum)
# print(chr(ascii_sum))



hash_value = "d"
ascii_value = ord(hash_value)
ascii_value = int((ascii_value/2)-50)
print(ascii_value)
before_mod = 0
while True:
    if before_mod % 11 == ascii_value:
        print(before_mod)
    before_mod += 1
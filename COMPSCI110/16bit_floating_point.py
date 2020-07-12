'''
author:Haiqiang Zhang
'''
def main():
    input_number = input("Please input the decimal number: ")
    if input_number[0] == "-":
        first_bit = 1
        input_number = input_number[1:]
        if "." in input_number:
            float_binary = float_dec2bin(float(input_number))
            int_binary = float(int_dec2bin(int(float(input_number))))
            binary = int_binary + float("0."+float_binary)
        else:
            binary = int_dec2bin(int(input_number))
        print("-", binary, sep="")
    else:
        first_bit = 0
        if "." in input_number:
            float_binary = float_dec2bin(float(input_number))
            int_binary = float(int_dec2bin(int(float(input_number))))
            binary = int_binary + float("0."+float_binary)
        else:
            binary = int_dec2bin(int(input_number))
        print(binary)
    print("floating point format:", bin_to_16bit_transition(first_bit, binary))
    print("hexadecimal:", hex(int("0b" + bin_to_16bit_transition(first_bit, binary), 2))[2:])
    print()
    return()

def int_dec2bin(dec):    # dec is int
    result = bin(dec)[2:]
    return result

def float_dec2bin(x):
    x -= int(x)
    bins = []
    while x:
        x *= 2
        bins.append(str(1 if x >= 1. else 0))
        x -= int(x)
    bins = ''.join(bins)
    return bins

def bin_to_16bit_transition(first_bit, binary):
    result = str()
    first_bit = str(first_bit)
    binary = str(binary)
    if "." in binary:
        point_index = binary.find(".")
        if point_index != 1:
            binary = binary[:point_index] + binary[point_index + 1:]
            result = first_bit + binary + "0"*(9 - len(binary)) + "0" + "0"*(5-len(str(int_dec2bin(point_index)))) + str(int_dec2bin(point_index))
        else:
            for index in range(2, len(binary)):
                if binary[index] != "0":
                    binary = binary[index:]
                    neg_exponent = index - 2
                    break
            result = first_bit + binary + "0"*(9 - len(binary)) + "1" + "0"*(5-len(str(int_dec2bin(neg_exponent)))) + str(int_dec2bin(neg_exponent))
    else:
        for index in range(-1, -len(binary)-1, -1):
            pos_index = len(binary) + index
            if binary[index] != "0":
                processed_binary = binary[:pos_index+1]
                break
        result = first_bit + processed_binary + "0" * (9 - len(processed_binary)) + "0" + "0" * (5 - len(str(int_dec2bin(len(binary))))) + str(int_dec2bin(len(binary)))

    return result


while True:
    main()
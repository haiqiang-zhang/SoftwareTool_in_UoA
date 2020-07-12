def main():
    while True:
        character = input("Input the character: ")
        rle_result_character = rle_character(character)
        compression_ration = len(character)/len(rle_result_character)
        print(rle_result_character)
        print("The Compression Ratio:", compression_ration)
    return

def rle_character(character):
    count_number = 1
    real_time_alphabet = str(character[0])
    rle_process = ""
    for index in range(1, len(character)):
        if character[index] != real_time_alphabet:
            rle_process = rle_process + real_time_alphabet + str(count_number)
            real_time_alphabet = character[index]
            count_number = 1
        elif index == len(character)-1:
            rle_process = rle_process + real_time_alphabet + str(count_number+1)
        else:
            count_number += 1
    return rle_process



main()

from pycipher import caesar
from tkinter import *

def de_caesar(input_text, key):
    if input_text.isupper() == True:
        plain_text = caesar.Caesar(key).decipher(input_text)
        plain_text = plain_text + "  key: " + str(key)
    else:
        plain_text = caesar.Caesar(key).decipher(input_text).lower()
        plain_text = plain_text + "  key: " + str(key)
    return plain_text

def en_caesar(input_text, key):
    if input_text.isupper() == True:
        cipher_text = caesar.Caesar(key).encipher(input_text)
        cipher_text = cipher_text + "  key: " + str(key)
    else:
        cipher_text = caesar.Caesar(key).encipher(input_text).lower()
        cipher_text = cipher_text + "  key: " + str(key)
    return cipher_text

def gui_tk():
    windows = Tk()
    windows.title("Caesar Cipher")
    windows.geometry("600x400")
    input_text_component = Entry(windows, show=None)
    input_text_component.place(x=32, y=50)
    text_component = Text(windows, height=26, width=40, bg='light grey', highlightbackground="black")
    text_component.place(x=300, y = 20)
    def de_caesar_button():
        text_component.delete(0.0, END)
        input_text = input_text_component.get()
        for index in range(1, 26):
            result_text = de_caesar(input_text, index) + "\n"
            text_component.insert("end", result_text)

    def en_caesar_button():
        text_component.delete(0.0, END)
        input_text = input_text_component.get()
        for index in range(1, 26):
            result_text = en_caesar(input_text, index) + "\n"
            text_component.insert("end", result_text)


    button_de_caesar = Button(windows, text="Decipher", width=10, height=2, command=de_caesar_button)
    button_de_caesar.place(x=80, y=150)
    button_en_caesar = Button(windows, text="Encipher", width=10, height=2, command=en_caesar_button)
    button_en_caesar.place(x=80, y=210)




    windows.mainloop()


if __name__ == "__main__":
    gui_tk()

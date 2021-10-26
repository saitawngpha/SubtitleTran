#!/usr/bin/python3
# author - T4wngPh4
# This project is using PyTranslator Libraries to translate the text.

from py_trans import PyTranslator
import re


def create_from_translate(text):
    """Create the output file with srt extension"""
    c_file = open(r'out-tran.srt', 'a')
    c_file.write(f"{text}\n")
    c_file.close()


def main():
    tran = PyTranslator()
    path_file = input("Enter your srt file with extension .srt: ")
    tran_lang = input("Enter your language code, example en, zh, de or th: ")
    file = open(fr'{path_file}').read().split("\n")
    pattern2 = "(\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})"
    # pattern = "(.*?[A-Z,a-z]+.*)+.*?"
    data = []
    pos = 0
    num_of_word = len(file)
    num_done = 0

    print("Start translating...")
    # loop for text in file list
    for text in file:
        if not re.match(pattern2, text) and re.match("[^0-9]", text):
            # find only text to translate
            text_tran = tran.translate(text, tran_lang)['translation']
            temp = {"text": text, "tran_text": text_tran}
            data.append(temp)
            # add the translate text to data dict
            num_done += 1
            print(f"Translate at: {num_done}/{num_of_word}")
        else:
            # no text to translate, example break line or enter
            data.append("")
            num_done += 1
            print(f"Translate at: {num_done}/{num_of_word}")
            # print(text, text_tran)
            # print(data)

    # to re-create file from translate text
    for word in file:
        # loop to get word from file list
        pos += 1
        # append 1 to pos variable every times from loop
        if not re.match(pattern2, word) and re.match("[^0-9]", word):
            # if text from file is equal to text from data list. Data list is from translate text
            print(data[pos - 1]['tran_text'], word)
            create_from_translate(data[pos - 1]['tran_text'])
        #   create file and add every text
        else:
            # the text is not equal to from data list
            print(word)
            create_from_translate(word)
            #   create file and add every text
    print("Your subtitle has been translated, please have a look at out-trans.srt!")


if __name__ == "__main__":
    main()

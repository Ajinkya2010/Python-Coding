import os
import re

class ReadCounter:
    def read_file():
        file = os.path.join(os.getcwd(),'TextInput.txt')
        input = open(file, 'r')
        out = input.readlines()
        return out

    def read_out():
        get_input = ReadCounter.read_file()
        clean_input = [line.split(" ") for line in get_input if type(line) == str]
        return clean_input

    def get_counter():
        get_input = ReadCounter.read_out()
        counter = {}
        for list in get_input:
            for word in list:
                word = re.sub('[^A-Za-z0-9]+', '' , word.strip())
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
        print(counter)

    def get_counter_for_input():
        counter = {}
        get_input = ReadCounter.read_out()
        string = str(input("Enter the value for the counter:\n"))
        for list in get_input:
            for word in list:
                word = word.strip()
                if word == string and word not in counter:
                    counter[word] = 1
                elif word == string and word in counter:
                    counter[word] += 1
                else:
                    continue
        print(counter)

    def case_func():
        var = input("Enter 1 : Get Counter for all the values in the text file\nEnter 2 : Get Counter of the Entered Input\n")
        options = {"1" : ReadCounter.get_counter(),
                   "2" : ReadCounter.get_counter_for_input()
        }
        return options[var]
    # map the inputs to the function blocks


def main():
    r1 = ReadCounter
    r1.case_func()

# Calling the main function
main()

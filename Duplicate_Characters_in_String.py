# Find the recurring character from the as_string
def get_rec(string):
    for count in range(len(string)):
        for count_in in range(count+1,len(string)):
            if string[count] == string[count_in]:
                print(string[count_in])

def main():
    string = "DBABAD"
    get_rec(string)


main()

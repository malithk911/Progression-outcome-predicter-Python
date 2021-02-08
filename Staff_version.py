"""I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
   Any code taken from other sources is referenced within my code solution."""

# Student ID: 2018412              Date:  28.11.2019

# variables
progress_count, trailer_count, retriever_count, exclude_count, max_count = 0, 0, 0, 0, 0
dic = {0: 'passed', 1: 'deferred', 2: 'failed'}

print("\n\n━━━━━━━━━━━━━━━━━━━━━━ STAFF VERSION ━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")


def progress_outcome():
    """This function first checks for range error by comparing the three inputs with elements in a list
        If there is no range error, then it checks if there is a total error and lets the user know it
        If there is no total error, then it checks the value and output the progression outcome"""

    global progress_count, trailer_count, retriever_count, exclude_count, max_count, dic

    # li = [passed, deferred, failed]
    li = [int(input("♦ Enter " + dic[i] + " marks" + (" " * (10 - len(str(dic[i])))) + ": ")) for i in range(3)]
    values = [value for value in range(0, 121, 20)]  # values = [0, 20, 40, 60, 80, 100, 120]

    for i in range(len(li)):  # iterate through list to check if range error
        if li[i] not in values:
            print("━━━━━━━━━━━━━")
            print("RANGE ERROR!")
            print("━━━━━━━━━━━━━")
            break
    else:
        if li[0] + li[1] + li[2] == 120:
            if li[0] == 120:  # if pass == 120
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Progress ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                progress_count += 1
            elif li[0] == 100:  # if pass == 100
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Progress - module trailer ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                trailer_count += 1
            elif li[2] < 80:  # if failed >= 80
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Do not Progress – module retriever ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                retriever_count += 1
            elif li[2] >= 80:  # if failed >= 80
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Exclude ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                exclude_count += 1
        else:  # if total error
            print("━━━━━━━━━━━━━━━━━")
            print("TOTAL INCORRECT!")
            print("━━━━━━━━━━━━━━━━━")


def histogram():
    """Function histogram() prints a horizontal histogram."""

    global progress_count, trailer_count, retriever_count, exclude_count

    outputs = [progress_count, trailer_count, retriever_count, exclude_count]
    name = ["Progress ", "Trailer ", "Retriever ", "Exclude "]
    print("\n\n━━━━━━━━━━━━━━━━━━ HORIZONTAL HISTOGRAM ━━━━━━━━━━━━━━━━━━━━━━\n")

    for i in range(4):  # for i in range(4): print ( name (number of inputs) : ****** )
        print("\n   " + name[i] + "(" + str(outputs[i]) + ")" + ":" + " " * (10 - len(str(name[i]))) + " ★ " *
              outputs[i])
    print("\r")

 
def inputs():
    """This function lets user input C to input a mark or Q to quit program and view histogram of entered inputs.
    If user enters an invalid input, program lets user know. This function prints total number of correct entries"""

    global progress_count, trailer_count, retriever_count, exclude_count

    while True:
        print("\r")
        user = input("\n⚫ Enter C for input or Q to quit :")
        if user == "C" or user == "c":  # if user inputs C
            progress_outcome()
        elif user == "q" or user == "Q":  # if user inputs Q
            histogram()
            print("\n══════════════════════════════════════════════════════════")  # total valid entries
            print("    Total Entries: ", progress_count + trailer_count + retriever_count + exclude_count)
            print("══════════════════════════════════════════════════════════")
            break
        else:
            print("━━━━━━━━━━━━━━━━━━━━")
            print("ENTER VALID INPUT!")
            print("━━━━━━━━━━━━━━━━━━━━")
            continue


while True:
    try:
        inputs()
        break
    except ValueError:  # if user input is not integers
        print("━━━━━━━━━━━━━━━━━━━━")
        print('INTEGERS REQUIRED!')
        print("━━━━━━━━━━━━━━━━━━━━")


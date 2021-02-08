"""I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
   Any code taken from other sources is referenced within my code solution."""

# Student ID: 2018412             # Date:  28.11.2019


print("\n\n━━━━━━━━━━━━━━━━━━━━━━━━━ STUDENT VERSION ━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")


def progress_outcome():
    """This function first checks for range error by comparing the three inputs with elements in a list
        If there is no range error, then it checks if there is a total error and lets the user know it
        If there is no total error, then it checks the value and output the progression outcome"""

    values = [value for value in range(0, 121, 20)]  # values = [0, 20, 40, 60, 80, 100, 120]

    for i in range(len(li)):  # iterate through list to check if range error
        if li[i] not in values:
            print("━━━━━━━━━━━━━")
            print("RANGE ERROR!")
            print("━━━━━━━━━━━━━")
            break
    else:
        if li[0] + li[1] + li[2] == 120:
            if li[0] == 120:  # if pass == 120 --> Progress
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Progress ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            elif li[0] == 100:  # if pass == 100 --> Module trailer
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Progress - module trailer ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            elif li[2] <= 60:  # every other combination
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Do not Progress – module retriever ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            elif li[2] >= 80:  # fail
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(" Progression outcome :- Exclude ")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        else:
            print("━━━━━━━━━━━━━━━━━")
            print("TOTAL INCORRECT!")
            print("━━━━━━━━━━━━━━━━━")


while True:
    """ Main program runs in an infinite while loop. Users can enter there marks (passed, deferred, failed) to
    check for progression outcome. Program gets user inputs into list. If ValueError, program lets user know """

    try:
        dic = {0: 'passed', 1: 'deferred', 2: 'failed'}
        print("\n")  # li = [passed, deferred, failed]
        li = [int(input("♦ Enter " + dic[i] + " marks" + (" " * (10-len(str(dic[i])))) + ": ")) for i in range(3)]
        progress_outcome()
        break
    except ValueError:
        print("━━━━━━━━━━━━━━━━━━━━")
        print('INTEGERS REQUIRED!')
        print("━━━━━━━━━━━━━━━━━━━━")

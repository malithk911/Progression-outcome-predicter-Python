"""I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
   Any code taken from other sources is referenced within my code solution."""

# Student ID: 2018412             # Date:  28.11.2019

# variables/lists
progress_count, trailer_count, retriever_count, exclude_count, max_count, error_count = 0, 0, 0, 0, 0, 0
li = ((120, 0, 0), (100, 20, 0), (100, 0, 20), (80, 20, 20), (60, 40, 20), (40, 40, 40), (20, 40, 60),
      (20, 20, 80), (0, 20, 100), (0, 0, 120))

print("\n\n═══════════════════ ALTERNATE STAFF VERSION ═════════════════════\n")


def histogram():
    """Function histogram() prints a horizontal histogram."""

    outputs = [progress_count, trailer_count, retriever_count, exclude_count]
    name = ["Progress ", "Trailer ", "Retriever ", "Exclude "]

    for i in range(4):
        print("\n   " + name[i] + "(" + str(outputs[i]) + ")" + ":" + " " * (10 - len(str(name[i]))) + " ★ " * outputs[i])
    print("\r")


def progress_outcome():
    """This function prints out a table of the all the marks; passed, deferred and failed as well as the prediction
    outcome of each entered combination."""

    global li, progress_count, trailer_count, retriever_count, exclude_count, error_count

    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("    Pass  ┃  Defer ┃  Fail  ┃ Progressive Outcome               ")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    try:
        for i in range(len(li)):
            print(("{}" + str(li[i][0]) + "{}" + str(li[i][1]) + "{}" + str(li[i][2])).format(
                    " " * (8-len(str(li[i][0]))),
                    " " * (8-len(str(li[i][1]))),
                    " " * (8-len(str(li[i][2])))), end="      ")  # end = " " prevents printing of new line

            if li[i][0] + li[i][1] + li[i][2] == 120:
                if li[i][0] == 120:  # if passed == 120
                    progress_count += 1
                    print("Progress")
                elif li[i][0] == 100:  # if passed == 100
                    trailer_count += 1
                    print("Progress - module trailer")
                elif li[i][0] >= 20 and li[i][2] < 80:  # if passed >= 20 and failed < 80
                    retriever_count += 1
                    print("Do not progress - module retriever")
                elif li[i][2] >= 80:  # if failed >= 80
                    exclude_count += 1
                    print("Exclude")
            else:
                print("Error!")
                error_count += 1  # count errors

        if error_count > 0:
            print("\n⚫ ERRORS IN", error_count, "INPUTS.\n")
        print("\n\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━ HISTOGRAM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")

    except TypeError or ValueError:  # if user input != integer
        print("\n\nERROR - INTEGERS REQUIRED AS INPUT.\n")
        print("\n\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━ HISTOGRAM ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")


progress_outcome()
histogram()
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

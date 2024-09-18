print("Let's grade this.")
while True:
    points_possible = input("What is the total points possible? ")
    points = input("How many points did they get? ")
    percentage = 100 * float(points)/float(points_possible) #I got this formula for percentages from Stack Overflow.
    if percentage < 51:
        print("F")
    elif percentage < 61:
        print("D")
    elif percentage < 76:
        print("C")
    elif percentage < 89:
        print("B")
    else:
        print("A")
    print("Let's grade another.")

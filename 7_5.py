def namen(studenten):
    studenten = input("Volgende naam: ")
    counters = {}
    for student in studenten:
        if student in studenten:
            counters[student] += 1
        else:
            counters[student] = 1


    return counters

namen()
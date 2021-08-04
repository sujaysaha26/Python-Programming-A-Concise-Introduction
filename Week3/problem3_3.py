def problem3_3(month, day, year):
    allMonth = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Semptember', 'October', 'November', 'December')
    myMonth = allMonth[month-1]
    print(str(myMonth), str(day) + ", " + str(year))
    
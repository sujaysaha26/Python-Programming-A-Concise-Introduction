def problem3_7(csv_pricefile, flower):
    import csv
    filename = open(csv_pricefile)
    for item in csv.reader(filename):
        if flower == item[0]:
            print(item[1])
    filename.close()
    
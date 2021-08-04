import sys

firstfile = sys.argv[1]
secondfile = sys.argv[2]

f1 = open(firstfile)
f2 = open(secondfile, 'w', newline='')

for line in f1:
    line = line.strip("\n")
    f2.write(str(len(line)) + "\n")

f1.close()
f2.close()
        
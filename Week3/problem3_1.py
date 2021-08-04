def problem3_1(txtfilename):
    letters = 0
    f = open(txtfilename)
    for word in f:
        letters = letters + len(word)
        print(word, end="")
    print()
    print("\nThere are", letters, "letters in the file.")
    
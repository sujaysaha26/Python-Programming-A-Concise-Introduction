# Loop to compute sum of numbers 1 through n

def problem1_3(n):
    add = 0
    for i in range(1, n+1):
        add += i
    print(add)
    
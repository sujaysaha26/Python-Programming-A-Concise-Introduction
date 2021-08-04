def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a = float(input("Enter lenght of side one: "))
    b = float(input("Enter lenght of side two: "))
    c = float(input("Enter lenght of side three: "))
    
    s = .5*(a + b + c)
    x = s*(s-a)*(s-b)*(s-c)
    area = x**.5
    print("Area of a triangle with sides", a, b, c, "is", area)
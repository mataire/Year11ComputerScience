total = 0
grade = " "

def acceptdata(total): #total is a parameter
    
    maths=int(input("Enter Maths Results: "))
    
    while maths < 0 or maths > 100:
        print("Value Should Be 0 - 100 ")
        maths=int(input("Enter Maths Results "))
    
    science=int(input("Enter Science Results: "))
    
    while science < 0 or science > 100:
        print("Value Should Be 0 - 100 ")
        science=int(input("Enter Science Results "))
    
    ict=int(input("Enter ICT Results: "))
    
    while ict < 0 or ict > 100:
        print("Value Should Be 0 - 100 ")
        ict=int(input("Enter ICT Results "))
    
    total = maths + science + ict
    
    return total # passes total to the next module


def calculations(grade):
    
    results=acceptdata(total)
    
    if results < 50:
        grade = "Fail "
    else:
        grade = "Pass "
    
    return(grade)

grades=calculations(grade)

print("Grade ", grades)

    
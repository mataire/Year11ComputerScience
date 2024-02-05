num1= int(input("Num 1 "))
num2= int(input("Num 2 "))
num3= int(input("Num 3 "))

if num1 == num2 :
    if num1 == num3:
        total = num1 * 3
        print("Total: ", total)
    else:
        total = num1 + num2 - num3
        print("Total: ", total)
        
elif num1 != num2 and num2 != num3 :
    print("Total: ", 0)
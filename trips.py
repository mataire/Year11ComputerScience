def acceptdetails():
    global name, method, adults, destin, trip, children
    
    name = input("Enter Name ")
    destin = input("Enter Destination ")
    trip = input("Enter Trip Type ")
    method = input("Enter Payment Method ")
    adults = int(input("Enter Number Of Adults "))
    children = int(input("Enter Number Of Children "))
    
def calculations():
    global total, creditpay, final
    
    nop = adults + children
    
    if destin =="p":
        if trip == "r":
            total = adults * 350 + children *350 / 2
        else:
            total = adults * 200 + children * 200 / 2
    elif destin == "a":
        if trip == "r":
            total = adults * 430 + children *430 / 2
        else:
            total = adults * 290 + children * 290 / 2
    else:
        total = 0
    
    if method == "c":
        final = total * 1.02
    else:
        final = total * 1.03
        
    if nop > 10:
        print("Plane Full ")
        final = 0
        
def printing():
    
    print("Running Print")
    print("Name :", name)
    print("Payment Method: ", method)
    print("Adults: ", adults)
    print("Children:", children)
    print("Destination:", destin)
    print("Trip ", trip)
    print("Cost: ", final)
    
acceptdetails()
calculations()
printing()
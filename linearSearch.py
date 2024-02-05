import random
ages = []
num = int(input("Enter Number Of Students "))

for count in range(num):
    age = random.randint(10,50)
    ages.append(age)

print(ages)
found = False
count = 0

def linear(data):
    found = False
    count = 0
    while count < num and not found :
        if ages[count] == data :
            found = True
        count +=1
    return(found)

search = int(input("Enter Number To Search "))
results = linear(search)

print("Results: ", results)
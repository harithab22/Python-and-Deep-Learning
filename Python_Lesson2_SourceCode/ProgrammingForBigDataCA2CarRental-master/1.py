lbs=[]
kgs=[]
n=int(input("Enter the number of students::"))
for i in range(n):
    num=int(input("Enter the value:"))
    lbs.append(num)
    kilograms=num * 0.454
    kgs.append(kilograms)
print("weight of the students in lbs:")
print(lbs)
print("weight of the students in kilograms:")
print(kgs)
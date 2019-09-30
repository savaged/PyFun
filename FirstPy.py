name = input("Name:")
age = input("Age:")
gender = input("Gender (f/m): ")
cl1 = []
cl2 = []
cl3 = []
cl4 = []
if gender == "m":
    if int(age) < 12:    
        cl1.append(name)
    else:
        cl2.append(name)
else:
    if int(age) < 12:
        cl3.append(name)
    else:
        cl4.append(name)
print("cl1->", cl1)
print("cl2->", cl2)
print("cl3->", cl3)
print("cl4->", cl4)

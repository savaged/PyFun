#accept name and surname here
name = input("Enter name: ")
surname = input("Enter surname: ")

#accept marks here
maths = int(input("Enter maths mark: "))
science = int(input("Enter science mark: "))
art = int(input("Enter art mark: "))
english = int(input("Enter english mark: "))
ict = int(input("Enter ict mark: "))

#find the average and total

total_marks = maths + science + art + english + ict
average = total_marks/5

#pass or fail?

if average < 50:
    grade = "F"
else:
    grade = "P"

#Output section
print("name: ", name)
print("surname: ", surname)
print("total marks: ", total_marks)
print("average: ", average)
print("grade: ", grade)


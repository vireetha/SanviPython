print("Enter Marks Obtained in 4 subjects")
Math = int(input("Maths:  "))
English = int(input("English: "))
Science = int(input("Science: "))
Hindi = int(input("Hindi: "))

sum = Math + English + Science + Hindi
print("Sum of math,english,sciene and hindi")

perc = (sum/400)*100

print(end="Percentage Mark= ")
print(perc)

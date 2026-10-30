name=input("enter student name: ")
marks=int(input("enter student marks: "))

print("student name:",name)
print("student marks:",marks)
if marks>=75:
    print("grade: A")  
elif marks>=60:
    print("grade: B")
else:
    print("grade: C")
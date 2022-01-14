#1. Write a Python program to find average of three numbers entered by the user.

print('             Program 1\n')

num1=float(input('Enter number: '))
num2=float(input('Enter number: '))
num3=float(input('Enter number: '))

avg=(num1+num2+num3)/3

print('\nAverage of the numbers is: ',round(avg,2))

#Q2. Write a python program to compute a person's income
print('\n             Program 2')

print('___INCOME TAX___')

print('''• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.''')

incm=float(input('\n\nEnter your income to the nearest penny(without commas): $'))

dpnd=int(input('Enter the number of dependents in family: '))

taxable_incm=incm-10000.00-(dpnd*3000)

if taxable_incm>0:
    print('Your taxable income is $',taxable_incm,sep='')
    tax=taxable_incm*0.2
    print('Income Tax =$',round(tax,2),sep='')
else:
    print("You don't have to pay income tax.\nThanks for using our service.")

#Q3. Write a python program to store different data type values into a list.

print('\n             Program 3\n')
student_lst=[]

N=int(input('Enter the number of students in class: '))

for i in range(N):
    sid=int(input('\nStudent ID: '))
    name=input("Student's Name: ")
    gender=input("Student's Gender\n[Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).]: ")
    course=input("Student's course: ")
    cgpa=float(input("Student's CGPA: "))

    student=[sid,name,gender,course,cgpa]

    student_lst=student_lst+[student]
print('\n\nStudent List:-\n',student_lst)

#Q4. Write a python program to enter marks of 5 students into a list and display them in sorted manner.
print('\n             Program 4\n')
lst=[]

for i in range(5):
    marks=input("Student marks: ")
    lst.append(marks)
lst.sort()
print("\nSorted List Of Student marks:-",lst,sep='\n')

#5. List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

print('\n             Program 5\n')

#a. Write a Python program to print a specified list after removing 4th element.
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("a.\n",color)

#b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.Do that in one line code.
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=["Purple"]
print("\nb.\n",color)

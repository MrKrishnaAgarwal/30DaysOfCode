from tkinter import Variable

n=Variable
n1= int(input("Enter 1st number: "))
n2= int(input("Enter 2nd number: "))
n3= int(input("Enter 3rd number: "))

maximum= max(n1,n2,n3)
minimum= min(n1,n2,n3)

print("The largest number is: ",maximum)
print("The smallest number is: ",minimum)
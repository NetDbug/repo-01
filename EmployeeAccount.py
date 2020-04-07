import random
import string

employees = []

def generatePassword(x):
	letters = string.ascii_letters
	rndmStrng=""
	preferredPassword=""
	for i in range(5):
		rndmStrng += random.choice(letters)

	print("Auto generated password: ", rndmStrng+x)	
	acceptPassword = input("Type 1 to accept password or 2 to enter a preferred password: ")
	if int(acceptPassword) == 1:
		return rndmStrng+x
	else:	
		preferredPassword = input("Enter password: ")
		while len(preferredPassword) < 7:
			print("Error! Password must be at least 7 characters long.")
			preferredPassword = input("Enter password: ")	
		return preferredPassword

def creatEmployee():
	firstName = input("Enter your first name: ")
	lastName  = input("Enter your last name: ")
	email     = input("Enter your email address: ")
	password = generatePassword(firstName[0:2]+lastName[len(lastName)-2:len(lastName)])
	employee =[firstName, lastName, email, password]
	
	return	employee		
		
	
employees.append(creatEmployee())
loop = "yes"
while loop == "yes":
	loop = input("Do you want to creat another employee?")
	if loop == "yes":	
		employees.append(creatEmployee())
print()
print("Sucessfully created employee account(s): ")
for i in employees:
		print()
		print("Name: ", i[0]+" "+i[1])
		print("Email: ", i[2])
		print("password: ", i[3])	
		print()
import random

#get aquestion from the user
input("What is your question for the Magic 8 Ball?")

#generate a random number
number=random.randint(1,3)
#print(number)

#give a response based on the random number
if number == 1:
	print("Yes")
elif number == 2:
	print("No")
else:
	print("Maybe")

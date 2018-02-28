
alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = 4

def choice():
	userChoice = raw_input("do you want to Encrypt or Decrypt? Enter e or d:  ").lower()
	if userChoice == "e":
		encrypt()
	elif userChoice == "d":
		decrypt()
	else:
		print"Invalid input"
	


def encrypt():

 	plaintext = raw_input('Please enter a message: ')

 	result = ' '
 	newMessage = ""
 	for i in plaintext:
		position = alphabet.find(i)

		newPosition = (position + key) % 25

		#print(newPosition)

		newCharacter = alphabet[newPosition]
		
		newMessage += newCharacter
	# else:
	# 	newMessage += character
	print'your new message is: ', newMessage



def decrypt():
	ciphertext = raw_input("Enter encrypted message: ")
	newMessage = ""


	for i in ciphertext:

		position = alphabet.find(i)
	
		# print "position = {0} c={1}".format(position, i)

		newPosition = (position - key) % 25

		# print "newPosition = {0} ".format(newPosition)

		newCharacter = alphabet[newPosition]
		# print newCharacter

		newMessage += newCharacter
	# else:
		# newMessage == character
	print'your new message is: ', newMessage


choice()
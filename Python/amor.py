answer = input("Do you love? (yes/no): ")

if answer.lower() == "yes" or answer.lower() == "y":
	print("That's wonderful! Love is a beautiful thing.")
elif answer.lower() == "no" or answer.lower() == "n":
	print("That's okay. Love is not for everyone.")
else:
	print("Invalid answer. Please enter 'yes' or 'no'.")
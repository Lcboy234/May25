import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""

# # using range to check how many nr_letters have been inputted, range() is normally based on if range is 12 then range() have to be range(1, 13)
# for character in range(1, nr_letters + 1):
#     #set a variable as random_character to choose how many times letters based on nr_letters
#     random_character = random.choice(letters)
#     #start adding random_character back to password
#     password += random_character

# # shorten version for for loop
# for char in range(1, nr_symbols + 1):
#     password = password + random.choice(symbols)

# # even shorter version
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# #print out the final version of password outside of for loop so it does not keep showing up
# print(password)

# change the whole string into list so it can be shuffled
new_password = []
for char in range(1, nr_letters + 1):
    # using append instead of += for list += is for string
    new_password.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    new_password.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    new_password.append(random.choice(numbers))

# cannot add new variable for shuffle(), just shuffle it without and print it again
random.shuffle(new_password)

# convert shuffled password into string in order to print them out without []

# set an empty string
final_password = ""

# for every character from the list
for char in new_password:
    # slowly add them back into the string
    final_password += char
#print the final one out
print(final_password)
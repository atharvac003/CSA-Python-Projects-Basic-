import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

final_lst=[]

for let in range(0,nr_letters):
  letter_element=random.randint(0,51)
  final_lst.append(letters[letter_element])

for num in range(0,nr_numbers):
  number_element=random.randint(0,9)
  final_lst.append(numbers[number_element])

for symb in range(0,nr_symbols):
  symbol_element=random.randint(0,8)
  final_lst.append(symbols[symbol_element])


for p in range(len(final_lst)-1, 0, -1):
   # getting a random index from 0 to the current index
   q = random.randint(0, p + 1)
   # Swap the current index element with the element at a random index so if p and q match they remain at the same index unaltered
   final_lst[p], final_lst[q] = final_lst[q], final_lst[p]

#this is a nice way of printing out each character of a list without any spaces, it conisders an empty string and keeps adding elements of
#the shuffled list to the string and then prints the entire concatenated string without any spaces in it

final_password= ""
for eachcharacter in final_lst:
  final_password+=eachcharacter

print(f"A possible password is: {final_password}")

#print(f"A possible password is: {''.join(final_lst)}")

#for printing the final list we can also easily use the random.shuffle command and then join list command as seen commented out above

from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continue_response="yes"
def translate(input_message,shift_amount,action):
  
  final_message=""
  if action=="decode":
     shift_amount*=-1
    
  for letter in input_message:
    if letter in alphabet:
        position=alphabet.index(letter)      
        new_position=position+shift_amount
        if new_position>25:
         final_message+=alphabet[new_position%26]
        elif new_position<0:
         final_message+=alphabet[new_position+26] 
        else:
         final_message+=alphabet[new_position] 
    else:
      final_message+=letter
      
  print(f"Here's {action}d text: {final_message}")

while continue_response:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  translate(input_message=text, shift_amount=shift,action=direction)
  continue_response=input("\nType 'yes' if you want to go again. Otherwise type 'no':\n")
  
print("Goodbye")  

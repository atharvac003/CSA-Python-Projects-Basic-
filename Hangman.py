import random
from replit import clear
from Hangmanwords import word_list
from Hangmanart import logo,stages

print(logo)

random_index=int(random.randint(0,len(word_list)-1))

random_word_as_string=word_list[random_index]


count=0
for i in range(0,len(random_word_as_string)):
  count+=1

length_of_chosen_word=int(count)
count_of_blanks=False


display=[]
for i in range(0,length_of_chosen_word):
     display+="_"
  
index=7
while not count_of_blanks:
 guess=input("\nGuess a letter: ").lower()
 clear()
 if guess in display:
      print(f"\nYou already guessed {guess}. Try another letter!")
   
 for i in range(0,length_of_chosen_word):
   
   if guess==random_word_as_string[i]:
      display[i]=guess
 print(f"\n{display}")
  
 if guess not in display:
    index-=1
    print(f"\n\n{guess} is not in the word. You lose a life!")
    print(f"{stages[index]}")
    if index==0:
       print("You lose!")
       print(f"\nThe correct word is {random_word_as_string}")
       count_of_blanks=True
    
 if "_" not in display:
    count_of_blanks=True
    print("\nYou win!")

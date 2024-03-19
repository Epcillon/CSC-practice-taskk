#Dictionary for storing questions and answers
niell={"1.What was Sam Niells first movie?\n a)Ivanhoe\n b)Jurassic Park\n c)The city of no\n d)Hunt for the wilderpeople":"c", 
       "2.What is Sam Niells nationality?\n a)Irish/English\n b)English/NZ\n c)NZ/Australian\n d)NZ/Irish":"d", 
       "3.In which Series did Sam Niell play an Irishmen?\n a)Merlin\n b)Peaky Blinders\n c)Ramsay\n d)The Crown":"b", 
       "4.What was his character's name in Jurassic Park?\n a)Alan Grant\n b)Bumbo Bamboli\n c)Richard Hammond\n d)Tyrannosaurus Rex Jr III":"a",
       "5.How old is he?\n a)65\n b)84\n c)56\n d)76":"d",}
#While loop for the quiz
quiz=input("Do you think you're qualified for this quiz?, y/n:")
if quiz!="y":
  exit()
play="y"
Name=input("Enter your name:")
print()
while "y" in play:
#For loop to ask questions, and recieve user answers
   score=0
   for x in niell:
      print(x)
      answer=(niell[x])
      guess=input("Enter a/b/c/d:").lower().strip()
      while guess not in ["a","b","c","d"]:
        print("Invalid input\n")
        guess=input("Enter a/b/c/d:").lower().strip()
      print()
#If statement for calculating score from answers
      if guess==answer:
        score+=1
        print("True\n")
      else:
       score+=0 
       print("False\n")
#Final scoring and passing, if score is 60% or above the user will pass
   print("You scored:",score*20,"%")
   print(score,"/",5, "Correct")
   if score>=3:
     print("Congratulations!",Name, ",You passed!")
     print()
   elif score<=2:
     print("You failed to pass, try again next time",Name)
     print()
#While loop repeats here, the code asks if  the user wants to play again
   repeat=input("Do you want to try again "+Name+"?, y/n:")
   print()
   if repeat!="y":
    exit()

# Quiz

Score = 0

# Q1
answer1 = input("who is your teacher? ")
if answer1 == "mr veldkamp" or answer1 == "Mr.v" :
    print("correct")
    Score = Score + 1
else:
    print("incorrect")

#Q2
answer2 = input("24+26 = ? ")
if answer2 == "50":
    print("correct")
    Score = Score + 1
else:
    print("incorrect")

#output score 
print("your score is" , Score/2 * 100 , "%.")
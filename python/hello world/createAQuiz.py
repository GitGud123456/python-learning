#Quiz
print("Welcome to chess Quiz!")
score = 0

Q1a = input("\n1. what is the most IMPORTANT piece in chess? ")
if Q1a.lower() == "king" or Q1a.lower() == "the king":
  print("Correct")
  score += 1
else:
  print("Wrong")

Q2a = input("\n2. what is the most POWERFUL piece in chess? ")
print(Q2a.lower())
if Q2a.lower() == "queen" or Q2a.lower() == "the queen":
  print("Correct")
  score += 1
else:
  print("Wrong")

Q3a = input("\n3. How many squares are on a chess board ")
if Q3a == "64":
  print("Correct")
  score += 1
else:
  print("Wrong")

Q4a = input(
  "\n4. what is the only piece in chess that can jump over other pieces? ")
if Q4a.lower() == "horse" or Q4a.lower() == "the horse" or Q4a.lower(
) == "knight" or Q4a.lower() == "the knight":
  print("Correct")
  score += 1
else:
  print("Wrong")

print("\nYOUR RESULTS:")
print(score, "/4  (", score / 4 * 100, "%)")

if score == 0:
  print("Never play chess")
elif score == 1:
  print("-10 ElO player")
elif score == 2:
  print("couple screws loose?")
elif score == 3:
  print("60 iq")
else:
  print("acceptable")


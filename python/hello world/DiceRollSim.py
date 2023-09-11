# pytrhon menu loop
loop = True
look_for_snake_eyes = False
while loop:
  #python print menu
  print("\nMAIN MENU")
  print("1: Roll Dice Once")
  print("2: Roll Dice Five Times")
  print("3: Roll Dice 'n' Times")
  print("4: Roll Dice until Snake eyes")
  print("5: EXIT")

  # Get Menu Selection from User

  selection = input("Enter Selection (1-5): ")

  # roll x num
  def roll2Dice(n):

    for _ in range(n):
      import random
      rand1 = random.randrange(1, 7)
      rand2 = random.randrange(1, 7)
      print("(" + str(rand1) + "," + str(rand2) + ") Sum:", rand1 + rand2)
      if look_for_snake_eyes and rand1 + rand2 == 2:
        return _

  # Take Action Based on Menu Selection

  if selection == "1":
    roll2Dice(1)
  elif selection == "2":
    roll2Dice(5)
  elif selection == "3":
    x = float(input("enter the number of times you want to roll the Dice: "))
    x //= 1
    roll2Dice(int(x))
  elif selection == "4":
    look_for_snake_eyes = True
    rolls = roll2Dice(10000000)
    print("snake eyes found after", rolls, "rolls.")
    look_for_snake_eyes = False
  elif selection == "5":
    print("\nEXIT")
    loop = False


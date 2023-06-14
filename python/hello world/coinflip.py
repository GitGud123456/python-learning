# python coin flip sim

import random

# Totals 
num_heads = 0
num_tails = 0


n = 1
while n <= 15:

    # flip coin
    randnum = random.randrange(1,3)
    if randnum == 1:
        print("heads")
        num_heads += 1
    else:
        print("tails")
        num_tails += 1

    # increment n
    n+=1

print("done. Number of heads:",num_heads, "Number of tails:", num_tails)


# for loop
for n in range(10):
    # loops 10 times
    print("hi")
   
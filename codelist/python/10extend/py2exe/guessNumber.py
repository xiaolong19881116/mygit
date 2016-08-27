import random
print "please guess a number in 0--99"
num = random.choice(range(100))
while True:
    g = int(raw_input("your number:"))
    if g==num:
        print "great!you win!"
        break
        
    if g > num:
        print "your number is too big!"
        
    if g < num:
        print "your number is too small!"

g = raw_input("BYE")
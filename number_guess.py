import random
number=random.randint(1,100)
while True:
    try:
        guess=int(input("guess a number between 1 to 100:"))
    except ValueError:
        print("Please enter  a valid number:")
    '''if guess==False:
        print("error")'''
    if(number<guess):
        print("too high")
    elif(number>guess):
        print("too low") 
    else:
        print("well done....!")      
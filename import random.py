import random

def guess (y):
    random_number = random.randint(1, y)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'GUess a number between 1 and {y}: '))
        if guess< random_number:
            print('TOo LOw')
        elif guess > random_number:
            print('tO hIgh')
        

    print('You did it, Congrats')
 
guess(10)

import random

min_val = 1
max_val = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print('Rolling thr Dice')
    print('The value is : ')
    
    print(random.randint(min_val, max_val))

    roll_again = input('Roll the Dice Again? ')

import random
def guess(x):
    random_number =random.randint(1,x)
    guess=0
    count=0
    while guess!= random_number:
        guess= int(input(f"guess a number between 1 and 50 :"))
        if guess > random_number:
            print('to high... try again ')
        elif guess<random_number:
            print('to low... try again')
        count=count+1
    print(f'wow you got it right and it only took you {count} times')

# guess(50)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 0
    while feedback!= 'yes':
        guess=random.randint(low,high)
        print(guess)
        feedback=input('am i right?')
        if feedback=='no':
            count=count+1
            feedback=input('can you tell me if it is higher or lower?')
            if feedback=='higher':
                low=guess+1
            elif feedback=='lower':
                high=guess-1
            else:
                print('thnaks for nothing')


    print(f'i beat you! XD in {count} tries')
# computer_guess(30)


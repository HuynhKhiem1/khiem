from random import randint
n = randint(1,100)
S = 0
limit = 10
while S < limit:
    player = int(input("Guess the number: "))
    if player == n:
        print("you win")
        quit()
    else:
        if player > n:
            print("Smaller")
            S = S + 1
        elif player < n:
            print("Bigger")
            S = S + 1
else:
    print("You lose")
    print("The random number is " + str(n))
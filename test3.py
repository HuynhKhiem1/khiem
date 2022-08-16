from random import randint
n = randint(1,100)
S = 0
limit = 10
while S < limit:
    player = int(input("Guess the number: "))
    if player == n:
        print("You win")
        break
    else:
        if player > n:
            print("Smaller")
            S = S + 1
        elif player < n:
            print("Bigger")
            S = S + 1
else:
    print("You lose")
    print("So random la " + str(n))
    quit()
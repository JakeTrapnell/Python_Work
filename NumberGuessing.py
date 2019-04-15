import random
max_rand = 10
min_rand = 0
secret_number = random.randint(min_rand, max_rand)
print(secret_number)
max_guesses = 3
guess_count = 0
print('guess the secret number between ' + str(min_rand) + ' and ' + str(max_rand))
while guess_count < max_guesses:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
        print('you win!')
        break
else:
    print('You lose! The secret number was: ' + str(secret_number))

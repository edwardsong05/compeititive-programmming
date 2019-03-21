# problem on kattis
# https://open.kattis.com/problems/hangman
# simulation

word = input()
guess = input()

unique_word = set()
unique_guess = set()

count = 0

for i in word:
    unique_word.add(i)

for i in guess:
    if i in unique_word:
        unique_guess.add(i)
    else:
        count += 1

    if len(unique_guess) == len(unique_word):
        print('WIN')
        break
    elif count == 10:
        print('LOSE')
        break

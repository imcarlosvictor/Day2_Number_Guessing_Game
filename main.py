import random


def main():

    player_tries: int = 0
    max_guess_range: int = int(input('Enter the maximum range: '))

    # Pick a random random_num
    random_num: int = random.randint(1, max_guess_range)

    while True:

        player_ans = int(
            input(f'Guess a number from 1 to {max_guess_range}: '))

        # Correct guess
        if player_ans == random_num:
            print(f'CORRECT! The random_num was {random_num}')
            print(f'Number of Tries: {player_tries}')
            break

        # Wrong guesses
        if abs(player_ans - random_num) <= 5:
            print('Warm!')
        elif abs(player_ans - random_num) <= 10:
            print('Cold!')
        elif abs(player_ans - random_num) > 10:
            print('Freezing!')

        player_tries += 1
        print('\n')


if __name__ == '__main__':
    main()

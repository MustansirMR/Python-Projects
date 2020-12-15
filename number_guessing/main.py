import random


class NumberGuessingGame:
    def __init__(self):
        self.score = 10

    def guess_number(self):
        self.num_to_guess = random.randint(2, 99)
        print(self.num_to_guess)
        print(f'I have a number in mind between 2 and 100. Can you guess it in {self.score} turns?')
        while True:
            try:
                guessed_num = int(input('Guess the number: '))
            except ValueError:
                self.reduce_score()
                self.check_end_game()
                print(f'Naughty Naughty! What you entered is not a number. You score is now {self.score}')
                continue
            if guessed_num == self.num_to_guess:
                print(f'You have guessed the number! Good job! Your score is {self.score}\n'
                      f'Thanks for playing the game!')
                break
            else:
                self.reduce_score()
                self.check_end_game()
                print(f'Not the number. Guess again. Your score is now {self.score}')
                self.print_hint()

    def print_hint(self):
        a = [self.get_multiple_hint, self.get_divisible_hint, self.get_lower_num, self.get_higher_num]
        print(f'Hint: {random.choice(a)()}')

    def get_multiple_hint(self):
        return f'{self.num_to_guess * random.randint(2, 20)} is a multiple of the number.'

    def get_divisible_hint(self):
        divisor_top_range = self.num_to_guess // 2 + 1
        divisors = [i for i in range(2, divisor_top_range) if self.num_to_guess % i == 0]
        if divisors:
            return f'{random.choice(divisors)} is a divisor of the number.'
        else:
            return 'The number is a prime number'

    def get_lower_num(self):
        return f'The number is higher than {random.randint(2, self.num_to_guess-1)}.'

    def get_higher_num(self):
        return f'The number is lower than {random.randint(self.num_to_guess+1, 99)}'

    def check_end_game(self):
        if self.score == 0:
            print("Oh no! You couldn't guess the number :( "
                  "But thanks for playing the game!")
            exit(0)

    def reduce_score(self):
        self.score -= 1


if __name__ == '__main__':
    random.seed()
    game = NumberGuessingGame()
    game.guess_number()
    # print(game.get_divisible_hint())


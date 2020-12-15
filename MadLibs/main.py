from typing import List


def mad_libs(phrases: List):
    noun = input('Enter a noun: ')
    pronoun = input('Enter an objective pronoun: ')
    verb1 = input('Enter a continuous verb: ')
    conjunction = input('Enter a conjunction: ')
    verb2 = input('Enter an indefinite verb: ')

    print(f'{phrases[0]}{noun} {phrases[1]}{pronoun} {phrases[2]}{verb1} '
          f'{phrases[3]}{conjunction} {phrases[4]}{verb2} {phrases[5]}')


if __name__ == '__main__':
    line_divided = [
        'There is no greater ',
        'to the critics and cynics and fearmongers than those of ',
        'who are ',
        'to fall ',
        'we have learned how to ',
        '.'
    ]
    mad_libs(line_divided)




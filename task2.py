# Programming task: Write a function that takes your birth year and current year
# as inputs and outputs your current age.

from datetime import datetime


def Age(birth_year):
    now = datetime.now().year
    print('Current year : ', now)
    current_age = now - birth_year
    print(f'Your age is {current_age}')


birth_year = int(input('Enter your birth year: '))
Age(birth_year)

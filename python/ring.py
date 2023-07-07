from random import randint

min_number = int(input('Please enter min: '))
max_number = int(input('Please enter max: '))

if (max_number < min_number):
    print('Invalid input - shutting down......')
else:
    rnd_number = randint(min_number, max_number)
    print(rnd_number)

    
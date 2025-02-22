def fizzbuzz(x):
    for i in x:
        for i in x:
            if i % 3 == 0 and i % 5 == 0:
                return 'FizzBuzz'
            elif i % 3 == 0:
                return 'Fizz'
            elif i % 5 == 0:
                return 'Buzz'
            else:
                return i
    else:
        'out of size'
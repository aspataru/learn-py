# learning python: https://docs.python.org/3/tutorial/

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(a)
        a, b = b, a + b
    return result


def get_fizz_buzz():
    x = int(input("Gimme: "))
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


def list_inserter(list):
    for word in list[:]:
        if len(word) > 2:
            list.insert(0, word + ', yo')


def mary_range():
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])


def prime_check(low, high):
    for x in range(low, high):
        for y in range(2, x):
            if x % y == 0:
                print(x, 'equals', y, '*', x // y)
                break
        else:
            # runs when no break occurs
            print(x, 'is a prime number')


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


def make_incrementor(n):
    return lambda x: x + n


def make_squares_list(max_range: int) -> list:
    return [x ** 2 for x in range(max_range)]


def pi_decimals(decs):
    from math import pi
    return [str(round(pi, x)) for x in range(1, decs)]


def set_minus(a_set: set, b_set: set) -> set:
    return {elem for elem in a_set if elem not in b_set}


def zip_example():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('What is your {0}?  It is {1}.'.format(q, a))


if __name__ == '__main__':
    zip_example()
    # print(set_minus(set('abra'), set('cada')))
# print(pi_decimals(10))
# print(make_squares_list(20))
# my_function = make_incrementor(42)
# print(my_function(3))
# ask_ok('bro?')
# prime_check(2,10)
# mary_range()
# print(fib(1000))
# getFizzBuzz()

# names = ['jo', 'al', 'ben', 'timmy']
# list_inserter(names)
# print(names)

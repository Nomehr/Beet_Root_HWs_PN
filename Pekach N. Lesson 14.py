# Lesson 14
## Task 1


def logger(func):
    def wrap(*args, **kwargs):
        print(f'Functions name: {func.__name__}')
    return wrap


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4,5)
square_all(4,5)

## Task 2


def stop_words(words: list):
    def decorator(func):
        def wrap(name: str):
            result = func(name)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrap
    return decorator


@stop_words(['pepsi','BMW'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print(create_slogan("Steve"))

## Task 3


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrap(arg):
            if not isinstance(arg, type_):
                print(f'Error. Argument should be {type_.__name__} type')
                return False
            if len(arg) > max_length:
                print(f'Error. Max length should be less then {max_length} symbols')
                return False
            for symbol in contains:
                if symbol not in arg:
                    print(f'Error. Argument has not a {symbol}')
                    return False
            return func(arg)
        return wrap
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f'{name} drinks pepsi in his brand new BMW!'


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

print(create_slogan('S@SH05'))
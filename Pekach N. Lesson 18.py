# Lesson 18
## Task 1

import re

class User:
    def __init__(self, email):
        self._email = None
        self.validate(email)

    def validate(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError(f"Invalid email address: {email}")
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self.validate(value)
        self._email = value

if __name__ == "__main__":
    try:
        user = User("valid.email@example.com")
        print(user.email)
        user.email = "new.email@domain.com"
        print(user.email)
        user.email = "invalid-email"
    except ValueError as e:
        print(e)

## Task 2

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return [worker.worker_info for worker in self._workers]

    @property
    def boss_info(self):
        return f"{self.name} from {self.company}"

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Only instances of Worker can be added.")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of the Boss class.")

    @property
    def worker_info(self):
        return f"{self.name} works at {self.company}, reporting to {self.boss.name}"

    def __repr__(self):
        return f"Worker(name={self.name}, company={self.company})"


boss1 = Boss(1, "Alice", "TechCorp")
worker1 = Worker(101, "Bob", "TechCorp", boss1)

print(worker1.worker_info)
print(boss1.workers)

worker2 = Worker(102, "Charlie", "TechCorp", boss1)
print(boss1.workers)

## Task 3

from functools import wraps

class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result in ['True', 'true', '1', 1, True]:
                return True
            elif result in ['False', 'false', '0', 0, False]:
                return False
            return bool(result)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                return float(result)
            except (ValueError, TypeError):
                return result
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
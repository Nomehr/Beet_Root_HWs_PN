# Lesson 21
## Task 1

import logging


class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.counter = 0
        logging.basicConfig(level=logging.INFO)

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            self.counter += 1
            logging.info(f"Opening file {self.filename} in {self.mode} mode. Open count: {self.counter}")
            return self.file
        except Exception as e:
            logging.error(f"Failed to open file {self.filename}: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            logging.error(f"An error occurred: {exc_value}")
        else:
            logging.info(f"File {self.filename} closed successfully.")

        if hasattr(self, 'file'):
            self.file.close()
        return True

## Task 2

import pytest
import os


def test_file_open_and_close():
    with FileContextManager("test_file.txt", "w") as file:
        file.write("Hello, world!")

    assert os.path.exists("test_file.txt")

    with open("test_file.txt", "r") as file:
        content = file.read()
    assert content == "Hello, world!"


def test_file_not_found():
    with pytest.raises(Exception):
        with FileContextManager("non_existent_file.txt", "r") as file:
            file.read()


def test_invalid_mode():
    with pytest.raises(ValueError):
        with FileContextManager("test_file.txt", "x") as file:
            file.write("This should raise an error")


def test_file_with_exception():
    with pytest.raises(ValueError):
        with FileContextManager("test_file.txt", "w") as file:
            file.write("This will work")
            raise ValueError("Test error")

## Task 3

def process_file_data(file_obj):
    data = file_obj.read()
    return data.upper()

@pytest.fixture
def file_fixture():
    with FileContextManager("test_file.txt", "w") as file:
        file.write("hello, world!")
    yield open("test_file.txt", "r")
    os.remove("test_file.txt")

def test_process_file_data(file_fixture):
    result = process_file_data(file_fixture)
    assert result == "HELLO, WORLD!"
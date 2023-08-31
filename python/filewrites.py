"""
Demonstrates performance improvements for code to write into files.
there are 3 approaches: writing line by line, writing all lines in 1 call
and writing in a buffered mode.
The code shows performace comparison between line by line vs all in one and 
line by line vs buffered mode
"""
from timeit import timeit
import inspect
import random
import string

def generate_random_strings(total_strings=5000, min_length=30, max_length=500):
    """
    Generate a list of total_length random strings.
    total_length: The number of strings to generate.
    min_length: minimum length of each random message
    max_length: maximum length of each random message
    returns: list of random strings
    """
    messages = []
    for _ in range(total_strings):
        length = random.randint(min_length, max_length)
        message = ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))
        messages.append(message)
    return messages

def write_to_file_linebyline(filename=None, list_data=None, append=False):
    """
    Slower version, writes line by  line
    """
    open_mode = 'w'
    if append:
        open_mode = 'a'
    try:
        with open(filename, open_mode, encoding='utf-8') as file_handler:
            for line in list_data:
                file_handler.write(line + "\n")
            file_handler.close()
    except OSError as error:
        print(f"Unable to write file {error.strerror}")  
    print(f"{inspect.currentframe().f_code.co_name}......Completed")


def write_to_file_allinone(filename=None, list_data=None, append=False):
    """
    Faster version, writes all in one call
    """
    open_mode = 'w'
    if append:
        open_mode = 'a'
    try:
        with open(filename, open_mode, encoding='utf-8') as file_handler:
            file_handler.write('\n'.join(list_data) + '\n')
        file_handler.close()
    except OSError as error:
        print(f"Unable to write file {error.strerror}")
    print(f"{inspect.currentframe().f_code.co_name}......Completed")


def write_to_file_buffer(filename=None, list_data=None, append=False, buffer_size=4096):
    """
    Write in buffered mode
    """
    open_mode = 'a' if append else 'w'
    try:
        with open(filename, open_mode, encoding='utf-8') as file_handler:
            buffer = []
            for line in list_data:
                buffer.append(line)
                if len(buffer) >= buffer_size:
                    file_handler.write('\n'.join(buffer) + '\n')
                    buffer = []
            if buffer:
                file_handler.write('\n'.join(buffer) + '\n')
    except OSError as error:
        print(f"Unable to write file {error.strerror}")
    print(f"{inspect.currentframe().f_code.co_name}......Completed")

if __name__ == "__main__":
    random_data = generate_random_strings(total_strings=55000)
    all_in_one = timeit('write_to_file_allinone(filename="allin1.txt", list_data=random_data)',
                        globals=globals(), number=1000)
    line_by_line = timeit('write_to_file_linebyline(filename="linebyline.txt", list_data=random_data)',
                          globals=globals(), number=1000)
    buffer =  timeit('write_to_file_buffer(filename="buffer.txt", list_data=random_data)',
                          globals=globals(), number=1000)
    speedup = line_by_line/all_in_one
    speedup2 = line_by_line/buffer
    print(f"All in on function execution time = {all_in_one} sec")
    print(f"Line by line function execution time = {line_by_line} sec")
    print(f"Buffer execution time = {buffer} sec")
    print(f"Speed up line by line vs all in one = {speedup}x")
    print(f"Speed up line by line vs buffer = {speedup2}x")

"""
All in on function execution time = 40.440192300011404 sec
Line by line function execution time = 190.0849691000185 sec
Buffer execution time = 64.13040620001266 sec
Speed up line by line vs all in one = 4.70x
Speed up line by line vs buffer = 2.96x
"""

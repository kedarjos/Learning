import timeit


def test_function():
    """
    This function will be called on line 26, where it will be imported
    and executed in a new namespace for timeit
    """
    for i in range(1000):
        pass


def test_timeit():
    """
    The code below will be called on line 24 where we pass
    empty setup and pass the entire code below to timeit
    """
    statment1 = """
def test_for_loop():
    for i in range(1000):
        pass
"""

    setup1 = "pass"
    print('1:', timeit.timeit(stmt=statment1, setup=setup1, number=10000))
    print('2:', timeit.timeit(stmt="test_function()",
                              setup="from __main__ import test_function",
                              number=10000))


if __name__ == "__main__":
    test_timeit()

"""
https://www.pylenin.com/blogs/python-timeit-module/
https://www.techgeekbuzz.com/blog/python-timeit-with-examples/
"""

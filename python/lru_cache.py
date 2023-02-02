from functools import lru_cache
import time


def fib(x):
    if x < 2:
        return x
    else:
        return fib(x-1) + fib(x-2)


@lru_cache(maxsize=128)
def fib_lru(x):
    if x < 2:
        return x
    else:
        return fib_lru(x-1) + fib_lru(x-2)


if __name__ == "__main__":
    print("Fibonacci series with and without LRU Cache")
    number = int(input("Enter a number: "))
    start_time_no_cache = time.time()
    [print(fib(i)) for i in range(number)]
    end_time_no_cache = time.time()

    start_time_cache = time.time()
    [print(fib_lru(i)) for i in range(number)]
    end_time_cache = time.time()

    print(f"Total Fibonacci numbers: {number}")
    print("Total time with cache:")
    no_cache_runtime = end_time_no_cache - start_time_no_cache
    print(f"--- {no_cache_runtime} seconds ---")
    print("Total time without cache:")
    cache_runtime = end_time_cache - start_time_cache
    print(f"--- {cache_runtime} seconds ---")
    difference = round(no_cache_runtime/cache_runtime, 2)
    print(f"--- {difference}x faster with cache ---")

"""
Total Fibonacci numbers: 35
Total time with cache:
--- 3.175370454788208 seconds ---
Total time without cache:
--- 0.004000663757324219 seconds ---
--- 793.71x faster with cache ---

Total Fibonacci numbers: 50
Total time with cache:
--- 6176.374272584915 seconds ---
Total time without cache:
--- 0.014039993286132812 seconds ---

https://realpython.com/lru-cache-python/#using-lru_cache-to-implement-an-lru-cache-in-python

"""

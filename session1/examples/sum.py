from timeit import timeit


def test_function():
    total = 0
    for i in range(10000000):
        total += i
    return total


def test_function_optimised():
    return sum(range(10000000))


if __name__ == "__main__":
    execution_time = timeit(test_function, number=1)
    print(f"Execution time: {execution_time} seconds")

    optimised_execution_time = timeit(test_function_optimised, number=1)
    print(f"Optimised execution time: {optimised_execution_time} seconds")

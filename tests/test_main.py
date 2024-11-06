from fizzbuzz import fizzbuzz


def test_run():
    assert fizzbuzz.run(1) == "1"

def test_run_multiple_of_three():
    assert fizzbuzz.run(3) == "Fizz"

def test_run_multiple_of_five():
    assert fizzbuzz.run(5) == "Buzz"

def test_run_multiple_of_three_and_five():
    assert fizzbuzz.run(15) == "FizzBuzz"
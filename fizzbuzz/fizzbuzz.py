def run(number: int):
    """
    If the number is a multiple of three, return the string "Fizz".
    If the number is a multiple of five, return the string "Buzz".
    If the number is a multiple of both three and five, return the string "FizzBuzz".

    Args:
        number (int): Number to convert

    Returns:
        str: conversion from number to string according to rules
    """

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    
    if number % 3 == 0:
        return "Fizz"
    
    if number % 5 == 0:
        return "Buzz"
    
    return f"{number}"


if __name__ == "__main__":
    for number in range (1,16):
        print(run(number))
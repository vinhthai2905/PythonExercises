# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    evens, odds = 0, 0
    for number in range(n):
        if number % 2 == 0:
            evens += 1
        elif number % 2 > 0:
            odds += 1
    print(f'The number of odds: {odds}, The number of evens: {evens}')

evens_and_odds(100)
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
number_sum = 0

for number in range(101):
    number_sum += number
else:
    print(number_sum)
# Use
# for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

sum_odds, sum_evens = 0, 0

for number in range(101):
    if number % 2 == 0:
        sum_evens += number
    else:
        sum_odds += number
else:
    print(sum_odds, sum_evens)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_age_list = bubble_sort(ages)
print(sorted_age_list)


# Add the min age and the max age again to the list
# Find the median age (one middle item or two middle items divided by two)
# Find the average age (sum of all items divided by their number )

sum_ages = sum(ages)
average_age = sum_ages/ages.__len__()
print(average_age)


# Find the range of the ages (max minus min)
# Compare the value of (min - average) and (max - average), use abs() method
# Find the middle country(ies) in the countries list
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
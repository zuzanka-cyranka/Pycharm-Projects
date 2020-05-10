def sum_of_positive_numbers(values):
    total = 0

    for value in values:
        if value < 0:       #value is smaller than 0, thus negative? oh, just ignore it and go further
            continue
        total += value      #adds up all the POSITIVE values to total

    return total            #returns the total sum of positive numbers

print(sum_of_positive_numbers([1, -2, 4, 90, -10]))
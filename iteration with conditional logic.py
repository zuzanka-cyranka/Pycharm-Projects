#returns the sum of odd numbers

values = [3,6,9,12,15,18,21,24]
other_values = [5,10,15,20,25,30]

def odd_sum(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:
            total = total + number
    return total



print(odd_sum(values)) #48
print(odd_sum(other_values)) #45


#returns the greatest or the largest number in the list

def greatest_number(numbers):
    for number in numbers:
        return max(numbers)

print(greatest_number([1,2,3,69, 420, -324]))


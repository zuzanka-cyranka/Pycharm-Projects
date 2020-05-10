# Write a factors function that accepts a positive whole number
# It should return a list of all of the number's factors in ascending order
# HINT: Could the range function be helpful here? Or maybe a while loop?
#
# factors(1)  => [1]
# factors(2)  => [1, 2]
# factors(10) => [1, 2, 5, 10]
# factors(64) => [1, 2, 4, 8, 16, 32, 64]

def factors(int:int):
    list_of_factors = []            #empty list that has to be filled with factors
    for number in range(1, int + 1):#for loop; it will loop through all numbers in the range of 1 to 10 (but doesnt include 10 so i added 1)
        if int  % number == 0:       #if the int (10) is dividable by number (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
            list_of_factors.append(number)  #it will append this number (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) to our empty list
        else:
            continue                #if the int is not dividable by number, let's just skip it and go back to the beginning of the function
    return list_of_factors

print(factors(10))
def create_phone_number(n):
    result = "({}{}{}) {}{}{}-{}{}{}{}".format(*n) #*n = all the ns
    return result
print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))
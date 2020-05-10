def fizzbuzz(number:int):
    count = 0
    while count < number:
        count +=1
        if count % 3 == 0 and count % 5 == 0:
            print("FizzBuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")
        else:
            print(count)

fizzbuzz()
def array_diff(array, item_to_remove):
    c = [x for x in array if x not in item_to_remove]
    return c
print(array_diff([1,2,2,2,2,2,2,5,4335], [2]))
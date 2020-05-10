meals = ["spaghetti", "bean soup", "bean soup", "bean soup", "curry", "lasagne"]
print(meals.count("bean soup"))

string = "zuzanna"
print(string.index("n"))

print(meals.index("bean soup"))

def all_indexes(list):
    bean_index = []
    for meal in meals:
        while "bean soup" == meal:
            bean_index.append(meals.index("bean soup"))
        continue
    return bean_index

print(all_indexes(meals))   #returns 1, 2, 3
breakfasts = ["Peanut butter and jelly", "Oatmeal", "Hummus on a toast"]
lunches = ["Apple", "Banana", "Smoothie"]
dinners = ["Curry", "Spaghetti", "Ramen"]

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    #for each element (breakfast, lunch, dinner) that share the same index position
    #iterate over within zipped lists (breakfasts, lunches, dinners)
    print(f"Today I ate {breakfast}, {lunch}, and {dinner}.")
    
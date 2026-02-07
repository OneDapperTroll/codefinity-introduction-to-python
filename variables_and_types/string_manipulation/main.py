grocery_items = "milk cheese bread apples oranges chicken"
#string slicing

dairy1 = grocery_items[0:5]
dairy2 = grocery_items[5:12]
bakery3 = grocery_items[12:18]

#Aisle number
aisle = 5

message = "we have dairy and bakery items:" \
+ dairy1 + ", " \
+ dairy2 + ", and " \
+ bakery3 \
+ " in aisle " \
+ str(aisle)

print(message)
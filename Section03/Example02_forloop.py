

# numberArray = [1,2,3,4,5 ]

# stringArray = ["lego","barbie","cars"]


# for x in stringArray:
#     print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
 

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print("1x: ", x)
#     if x == "banana":
#         break
# print ("2x: ", x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#     if x == "banana":
#         continue
#     print ("fruits: ", x)

# for x in range(6):
#     print(x)
  

 
 
for i in range(1, 11):
 
    # If i is equals to 6,
    # continue to next iteration
    # without printing
    if i == 6:
        continue
    else:
        # otherwise print the value
        # of i
        print(i, end=" ")
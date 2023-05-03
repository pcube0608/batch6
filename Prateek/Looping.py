
items = [1,2,3,7,8]

for item in items:
    if item == 2:
        continue
    print(item)


#
# for i in range(5):
#     print(items[i])

## break - to break the loop
## continue the loop


#while loop

condition = True
while condition == True:
    print("test")
    condition = False
print("hello")



count = 0
while count<=4:
    print("test")
    if count<2:
        count = count+1
    else:
        continue

print("hello")
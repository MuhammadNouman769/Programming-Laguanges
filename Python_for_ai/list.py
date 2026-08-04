
from readline import insert_text


list1 = [1, 2, 3, 4, 5]
print(list1)

# order of index
print(list1[0])

# mutable nature of list
list1[0] = 10
print(list1)

list1[4] = 50
print(list1) 

# its can store multiple data types
list2 = [1, 2, 3, "hello", 4.5]
print(list2)

#   it can store duplicate values
list3 = [1, 2, 3, 4, 5, 1, 2, 3]
print(list3)

# traversing on list
for i in list1:
    print(i)

    # travrersing on list using index
for i in range(len(list1)):
    print(f"list1[{i}]: {list1[i]}")  

# crud operations on list

list4 = [4,53,5,6,2,7, 1, 2, 4, 5]
# add element in list
list4.append(6)
# add element in list at specific index like 2
list4.insert(2, 3)
# pop element from list
list4.pop(1)
print(list4)
# remove element from list
list4.remove(5)
print(list4)
# sort list in ascending order
list4.sort()
print(list4)

l = [3, 4,1, -5, -6, 7, 2, 0]

pos = []
neg = []

for i in l:
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)

print("Positive numbers:", pos)
print("Negative numbers:", neg)

list5 = [10, 20, 30, 40, 50]

sum = 0
for i in list5:
    sum = sum + i
avg = sum / len(list5)
print(f"Sum: {sum}")
print(f"Average: {avg}")

number = [10,30,90, 20, 50, 70, 40, 60, 80]
index = 0
largest = number[0] 
for i in range(len(number)):
    if number[i] > largest:
        largest = number[i]
        index = i
print(f"Largest number: {largest} at index: {index}")


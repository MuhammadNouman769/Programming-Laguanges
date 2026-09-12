
""" ================ List =============== """
'''

1. List kia hai 
Answer: list aik order mutable collection hai 
Example.i

'''
from curses import has_ic


names = ["Ali", "Ahmad", "Usama"]
print(names)

'''
list ki properties:
      i. order
     ii. Mutable
    iii. duplicate allowed
     iv. defferent data types store

list create karne ka tarika
'''
a = [1, 2, 3]

'''
2.append() method kia hai
Answer: End pe aik item add krta hai

Example:i

'''
nums = [1, 2, 3]
nums.append(4)
print(nums)

'''
3. extend() method kia hai
Answer: extend() method multiple items add krta hai

Example:i
'''
number = [1, 2]
number.extend([3, 4])
print(number)

'''
4. insert method kia hai
Answer: insert() method specific index par add krta hai 

Example.i
'''
a = [1, 3, 4]
a.insert(1, 2)

'''
5. remove() method kia krta hai 
Answer: value remov krta hai

Example.i
'''
a = [1, 2, 3]
a.remove(3)
print(a)

'''
6. pop() method kia hai 
Answer: index se remove krta hai or value return krta hai 
Example.i
'''
a = [1, 2, 3, 4]

x = a.pop(0)
print(x)

''' 
spacific index remove kr dain ga
'''

a.pop(0)
print(a)

'''
7. clear() method kia krta hai 
Answer: list empty kr deta hai
Example.i
'''
a = [1, 2, 3, 4]

a.clear()
print(a)

'''
8. index() method kia krta hai
Answer: position btata hai

Example.i
'''
a = [1, 2, 3]

print(a.index(1))

'''
9. count() method kia krta hai
Answer: kitni dafa item aya

Example.i
'''

a = [1, 2, 3, 3, 3, 4]

print(a.count(3))

'''
10. sort() or sorted() method kia krta hai 
ascending 
descending
Example.i
'''

a = [4, 3, 2 ,1]

a.sort()
print(a)

a.sort(reverse=True)
print(a)



a = [4, 2, 1]

b = sorted(a)

print(a)
print(b)


'''
Interview Question

sort()         vs             sorted()

sort()                  	sorted()
Original list change	      New list return
List method	                  Built-in function


11. reverse() method kia hai 
Answer: list ko ult krta hai 

Example.i
'''

a = [1, 2, 3]

a.reverse()
print(a)


'''
12.join() ki hai

Answer: join list method nahi hai. Ye string method hai
ye do string ko jorta hai
Example.i
'''
names = ["Ali", "Ahmed", "Usama"]

result = ",".join(names)

print(result)

'''
13. split() method kia hai 
Answer: String ko list me convert karta hai.
Interview Question

split aur join opposite hain?

Han
Example.i
'''
data = "Ali Ahmed Usama"

result = data.split()

print(result)

'''
slicing
'''
a = [1, 3, 4, 5, 6, 7]

print(a[-1])
print(a[1:3])
print(a[1])
print(a[::-1])

'''
nested list
'''


data = [
    [1, 2],
    [3, 4]
]

print(data[1][0])
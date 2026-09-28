

# # result = 'even' if a % 2 == 0 else 'odd'
# print(result)

list1 = [1,4,2,5,6,8,5,9,3,1,2,3,98]    
large = 0

for i in list1:
    large = large + i
    if large != i:
        print(f'largest {large}')
    else:
        ('error')    
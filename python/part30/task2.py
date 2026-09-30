data = ["a", "b", "c"]

it = iter(data)
while True:
    try:
        item = next(it)
    except StopIteration:
        break
    print(item)


datas = [1,2,3,4,5]
index = 0
iter  = iter(datas)
while True:
    try:
        number = next(iter)
        index = index + 1
    except StopIteration:
        break
    print(f"value {number} index {index}")

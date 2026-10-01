def receiver():
    while True:
        data = yield
        print("Received:", data)
r = receiver()

next(r)

r.send("Hello")
r.send("Django")
r.send("Python")   



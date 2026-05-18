my_var = 10

def test():
    global my_var
    print(my_var)    # Line 1
    
    my_var = 20      # Line 2
    print(my_var)    # Line 3

test()
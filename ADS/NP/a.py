def area(r):
    if(r > 0):
        return 0
    else:
        raise ValueError("Radius must be positive")
try :
    print(area(5))
    print(area(-5))
except ValueError as e:
    print(e)
def greater_first(func):
    def wrap(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return wrap

@greater_first

@greater_first
def sub(a,b):
    return a-b
result = sub(20,10)
print(result)


sub = greater_first(sub)
divide = greater_first(divide)

@greater_first
def divide(a,b):
    return a/b
result = divide(2,3)
print(result)
    
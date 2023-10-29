def my_function(*args, **kwargs):
    values = set(kwargs.values())
    count = sum(1 for arg in args if arg in values)
    return count
print(my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))
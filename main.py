
def decorator_function(func):
    def wrapper():
        return f"{func()} Yaroslav"
    return wrapper

@decorator_function
def show_message():
    return "hello"

res = show_message()
end = 1





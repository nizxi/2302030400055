def person_info(*args, **kwargs):
    print("Names:")
    for name in args:
        print(name)
    print("\nAdditional Info:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling function with both args and kwargs
person_info("Alice", "Bob", age=25, city="New York")
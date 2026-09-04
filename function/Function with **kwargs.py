def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")

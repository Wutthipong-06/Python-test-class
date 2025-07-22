def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
display_info(name="Bank", age=18, city="Ban na")
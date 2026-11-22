def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krishna Sai", age=20, city="Vijayawada")

def shopping_cart(**products):
    total = 0
    print("Items Purchased:")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
        total += price
    print(f"Total: ₹{total}")

shopping_cart(apple=18, orange=7, mango=10, banana=8, grapes=20)

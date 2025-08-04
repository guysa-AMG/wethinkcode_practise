
prices={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
Total=0.00

while True:
    try:
        value = input("Item: ").title()
        if value in prices:
            Total+=prices[value]
            print(f"Total: ${Total:.2f}")
    except EOFError:
        break
def main():
    data = input("greeting: ")
    cost = value(data)
    print(f"${cost}")


def value(greeting):
    greeting=greeting.lower()
    if "hello" in greeting:
        if not greeting[:greeting.index("hello")].isalpha():
            return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

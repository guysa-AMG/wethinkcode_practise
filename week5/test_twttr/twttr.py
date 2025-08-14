
def main():
    message = input("input: ")
    data = shorten(message)
    print(data)


def shorten(word):
    vowels = ["a","e","i","o","u"]
    return "".join([char for char in word if not char.lower() in vowels])


if __name__ == "__main__":
    main()

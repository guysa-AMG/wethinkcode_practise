
def thought(data):
    parsed=data.lower()
    if "forty" in parsed and "two" in parsed:
        return "Yes"
    elif "42" in parsed:
        return "Yes"
    else:
        return "No"

prompt="What is the Answer to the Great Question of Life, the Universe, and Everything? "
value=input(prompt)

response=thought(value)

print(response)
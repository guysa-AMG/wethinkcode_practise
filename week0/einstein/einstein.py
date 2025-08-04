
def emc_sq(inp):
    c=3*10**8
    e=inp*c**2
    print(f"E: {e}")
    return e

value = int(input("m: "))
emc_sq(value)
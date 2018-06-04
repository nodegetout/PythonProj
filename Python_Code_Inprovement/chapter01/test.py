def f(x):
    return {
        0: "you typed zero!",
        1: "you are in top!",
        2: "n is an even-number!"
    }.get(x,"Only single-digital numbers are allowed.\n")

print(f(5))
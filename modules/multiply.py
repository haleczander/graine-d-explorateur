results = {}

def multiply(a, b):
    if (a, b) in results:
        return results[(a, b)]
    else:
        results[(a, b)] = a * b
        return results[(a, b)]
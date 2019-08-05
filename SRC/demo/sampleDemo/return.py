
def do_all(action):
    return {"sum": sum, "max": max, "min": min}[action]

print(do_all("sum")([5, 6]))
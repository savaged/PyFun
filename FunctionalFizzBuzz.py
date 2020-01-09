
def getVerb(i):
    value = ""
    r = i % 3
    if r == 0:
        value = "Fizz"
    r = i % 5
    if r == 0:
        value = value + "Buzz"
    if value == "":
        value = i
    return value

def getVerbs(integers = []):
    verbs = []
    for i in integers:
        verbs.append(getVerb(i))
    return verbs

def main():
    start = int(input("start: "))
    iterations = int(input("iterations: "))
    end = start + iterations
    integers = range(start, end)
    verbs = getVerbs(integers)
    for verb in verbs:
        print(verb)
    print("Done!")

main()

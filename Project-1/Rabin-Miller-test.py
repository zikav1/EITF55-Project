import random

def testRM(n):
    s = set()

    while len(s) < 20:
        a = random.randint(2,n-2)
        s.add(a)
    return s

print(testRM(13))
print("hej")
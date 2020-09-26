from collections import Counter
def checkIfCanBreak(s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        print(c1)
        c2 = Counter(s2)
        print(c2)
        diff = 0
        s = set()
        for i in range(26):
            c = chr(ord('a') + i)
            print(c)
            diff += c1[c] - c2[c]
            print(diff)
            if diff:
                s.add(diff > 0)
                print(s)
        return len(s) < 2
a='abc'
b='xya'
res=checkIfCanBreak(a,b)
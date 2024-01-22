class CountFromBy:
    def __init__(self, v: int=0, i: int=1) -> None:
        self.val = v
        self.incr = i


    def increse(self) -> None:
        self.val += self.incr


    def __repr__(self) -> str:
        return str(self.val)
    

k = CountFromBy()
k.increse()
print(k)

l = CountFromBy(100)
l.increse()
print(l)

m = CountFromBy(100, 10)
m.increse()
print(m)

n = CountFromBy(i=15)
n.increse()
print(n)
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        
a= Counter()
b= Counter()
c= Counter()

a.increment()
a.increment()
print(a.count)
print(b.count)
print(c.count)
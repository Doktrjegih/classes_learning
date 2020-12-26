class A:
    def __init__(self, i):
        print("Hello from init with i" + str(i))
        self.i = i
        
    def foo(self):
        print("Hello from foo with i" + str(self.i))
        

aList = []
print("Add element 1")
aList.append(A(1))
print("Add element 2")
aList.append(A(2))

for a in aList:
    a.foo()

# Add element 1
# Hello from init with i1
# Add element 2
# Hello from init with i2
# Hello from foo with i1
# Hello from foo with i2

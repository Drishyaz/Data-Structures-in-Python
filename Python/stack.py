class stack:
    def __init__(self):
        self.top = -1
        self.stacc = []
        
    def push(self,item):   
        self.stacc.append(item)
        self.top += 1
        print("Element pushed")
        
    def pop_stacc (self):
        if self.top == -1:
            print("Stack empty! Nothing to pop")
        else:
            self.stacc.pop(self.top)
            self.top -= 1
            print("Element popped")
        
    def isEmpty(self):
        if len(self.stacc) == 0:
            print("Empty")
        else:
            print("Not empty")
        
    def display(self):
        if len(self.stacc) == 0:
            print("Stack empty")
        else:
            l = [i for i in self.stacc[::-1]]
            for i in l:
                print(i)

    def reverse(self):
        if len(self.stacc) == 0:
            print("No item in stack")
        else:
            l = [i for i in self.stacc[::]]
            for i in l:
                print(i)
        
l = stack()
while True:
    print("[1] Push")
    print("[2] Pop")
    print("[3] Check if empty")
    print("[4] Display stack")
    print("[5] Reverse")
    print("[6] Exit")
    try:
        ch = int(input("Enter your choice: [1-6]\n"))
    except ValueError:
        print("Wrong choice!! Please try again!!")
    else:
        if ch == 1:
            item = int(input("Enter item: "))
            l.push(item)
        elif ch == 2:
            l.pop_stacc()
        elif ch == 3:
            l.isEmpty()
        elif ch == 4:
            l.display()
        elif ch == 5:
            l.reverse()
        elif ch == 6:
            print("Program terminated...")
            break
        else:
            print("Wrong choice!! Please try again!!")
        

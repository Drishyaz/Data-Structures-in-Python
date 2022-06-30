def linear(l,item):
    if item in l:
        for i in l:
            if i == item:
                indx = l.index(item)
                print("Item",item,"found at index",indx)
    else:
        print("Item not found in list")

def binary(lst1,item):
    l = len(lst1)
    lp,up = 0,l-1
    mp = (up+lp)//2
    
    if item not in lst1:
        print("Item not found in list")
        
    elif item >= lst1[mp]:
        for i in range(mp,l):
            if lst1[i] == item:
                print("Item",item,"found at index",i)
            
    elif item < lst1[mp]:
        for i in range(mp):
            if lst1[i] == item:
                print("Item",item,"found at index",i)
                
def traverse(l):
    print("Traversing the list: ")
    print(l[:])
    
def main():
    l = list(map(int,input("Enter a list: ").split()))
    while True:
        print("\n[1] Linear search")
        print("[2] Binary search")
        print("[3] Traverse list")
        print("[4] Quit")
        try:
            ch = int(input("\nEnter your choice: "))
        except ValueError:
            print("\nWrong choice!!")
        else:
            if ch == 1:
                item = int(input("Enter item to search for: "))
                linear(l,item)
            elif ch == 2:
                lst = sorted(l)
                print("Sorted list:",lst)
                item = int(input("Enter item to search for: "))
                binary(lst,item)
            elif ch == 3:
                traverse(l)
            elif ch == 4:
                print("Program terminated...")
                break
            else:
                print("Wrong choice!!")
    
if __name__ == '__main__':
    main()

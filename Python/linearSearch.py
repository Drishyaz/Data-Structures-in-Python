def linear(l,item):
    if item in l:
        for i in l:
            if i == item:
                indx = l.index(item)
                print("Item",item,"found at index",indx)
    else:
        print("Item not found in list")

def traverse(l):
    print("Traversing the list: ")
    print(l[:])

def main():
  item = int(input("Enter item to search: "))
  l = map(int,input().split())
  linear(l,item)
  
if __name__ == '__main__':
  main()

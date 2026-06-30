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
  item = int(input("Enter item to search: "))
  l = map(int,input().split())
  binary(l,item)
  
if __name__ == '__main__':
  main()

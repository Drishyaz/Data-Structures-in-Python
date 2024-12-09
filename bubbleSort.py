# ar = [int(input(f"Print the {i}th element: ")) for i in range(5)]
print("Enter array elements: ")
ar = list(map(int, input().split()))

n = len(ar)
print(f"Array before sorting: {ar}")
for i in range(n):
    for j in range(n-1):
        if ar[j] > ar[j+1]:
            temp = ar[j]
            ar[j] = ar[j+1]
            ar[j+1] = temp

print(f"Array after sorting: {ar}")

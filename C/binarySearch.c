// Binary Search
#include <stdio.h>
#include <stdbool.h>

void main() {
  int ar[] = {5,16,20,22,34,50};
  int len = sizeof(ar)/sizeof(int), key;  // key = 34, len = 6
  int first = 0, last = len-1; // first = 4, last = 5
  int mid = (first+last)/2;    // mid = 5
  bool found = false;
  
  scanf("%d",&key);
  
  if (ar[mid] == key)
  {
    printf("Found at index %d",mid);
    found = true;
  }
  else
  {
    while (first < last)
    {
      if (ar[mid] > key)
        last = mid - 1;
      else if (ar[mid] < key)
        first = mid + 1;
      else
      {
        found = true;
        printf("found at index %d",mid);
        break;
      }
      mid = (first + last)/2;
    }
  }
  
  if (found == false)
    printf("Did not find");
}

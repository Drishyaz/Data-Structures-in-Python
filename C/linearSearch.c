// Linear Search
#include <stdbool.h>
#include <stdio.h>

void main() {
  int ar[] = {50,20,16,34,22,5};
  int len = sizeof(ar)/sizeof(int), key;
  bool found = false;
  
  scanf("%d",&key);
  
  for (int i=0;i<len;i++)
  {
    if (key == ar[i])
    {
      printf("Found at index %d",i);
      found = true;
      break;
    }
  }
  
  if (found == false)
    printf("Did not find");
}

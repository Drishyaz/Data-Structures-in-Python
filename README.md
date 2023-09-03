# Data-Structures-in-Python

## Stack

### Components of Stack:

- **top** -> topmost element in the stack

### Operations on Stack:

- **push()**    -> Add element in top of stack
- **pop()**     -> Delete elemenet from top of stack
- **top()**     -> Return top element of stack without deleting it
- **isEmpty()** -> Checks if Stack is empty / Underflow
- **isFull()**  -> Checks if stack is full / Overflow

### Algorithms:

- **push():**
```
1. Check ifFull(). If yes, return "Overflow"
2. Else, Increment top
3. Push item to top
```

- **pop():**
```
1. Check ifEmpty(). If yes, return "Underflow"
2. Else, Let temp = stack[top]
3. Decrement top
4. Delete temp
```

- **top():**
```
1. Check ifEmpty(). If yes, return "Underflow"
2. Else, Let temp = stack[top]
3. Print temp
```

- **isEmpty():**
```
1. Check if top == -1
2. If yes, return "Empty" or "Underflow"
3. Else, return False
```

- **isFull():**
```
1. Check if top == max_size.
2. If yes, return "Full" or "Overflow"
3. Else, return False
```
### Implementation

- [x] using Array 
- [ ] using LinkedList

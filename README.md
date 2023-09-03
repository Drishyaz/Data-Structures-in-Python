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

## Simple Queue

### Components of Simple Queue:

- **front** -> front end of the queue, pointing to first element
- **rear**  -> front end of the queue, pointing to last element

### Operations on Simple Queue:

- **enqueue()** -> Add element in rear of queue
- **dequeue()** -> Delete elemenet from front of queue
- **peek()**    -> Print all elements of queue without deleting any
- **isEmpty()** -> Checks if Queue is empty
- **isFull()**  -> Checks if Queue is full

### Algorithms:

- **enqueue():**
```
1. Check ifFull(). If yes, return "Full"
2. Else, For the first element, set Front = 0
3. Increment rear
4. Add item to queue[rear]
```

- **dequeue():**
```
1. Check ifEmpty(). If yes, return "Empty"
2. Else, Let temp = queue[front]
3. Increment front
4. Delete temp
```

- **peek():**
```
1. Check ifEmpty(). If yes, return "Empty"
2. Else, loop through items of queue, from front to rear
3. Print each item
```

- **isEmpty():**
```
1. Check if front == -1 and rear == -1
2. If yes, return "Empty"
3. Else, return False
```

- **isFull():**
```
1. Check if rear == max_size
2. If yes, return "Full"
3. Else, return False
```
### Implementation

- [ ] using Array 
- [ ] using LinkedList

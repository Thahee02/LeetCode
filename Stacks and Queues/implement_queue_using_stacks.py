# class MyQueue(object):

#     def __init__(self):
#         # Initialize your data structure here.
#         # Add 2 stacks, one for input and one for output
#         self.stack_in = []
#         self.stack_out = []

#     def push(self, x):
#         # Push element x to the back of queue.
#         self.stack_in.append(x)

#     def pop(self):
#         # Remove the element from the front of the queue and return it.
#         # If the output stack is empty, we need to transfer all elements from the input stack to the output stack
#         if not self.stack_out:
#             while self.stack_in:
#                 self.stack_out.append(self.stack_in.pop())
#         return self.stack_out.pop()
    
#     def peek(self):
#         # Get the front element.
#         # If the output stack is empty, we need to transfer all elements from the input stack to the output stack
#         if not self.stack_out:
#             while self.stack_in:
#                 self.stack_out.append(self.stack_in.pop())
#         return self.stack_out[-1]
    
#     def empty(self):
#         # Returns whether the queue is empty.
#         # The queue is empty if both stacks are empty.
#         return not self.stack_in and not self.stack_out
        

# O(1) time complexity for push, O(n) for pop and peek in the worst case when we need to transfer elements from stack_in to stack_out, and O(1) for empty.
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val) 
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
    def getMin(self):
        return self.min_stack[-1]

# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
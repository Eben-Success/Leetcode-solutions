class MyQueue:

    # Time complexity is O(1) amortizeed
    # Space complexity is O(2n)
    
    def __init__(self):
        self.input = []
        self.output = []
        

    def push(self, x: int) -> None:
        self.input.append(x)
        

    def pop(self) -> int:
        n = len(self.input) - 1
        for i in range(n):
            self.output.append(self.input.pop())
        res = self.input.pop()
        for i in range(n):
            self.input.append(self.output.pop())
        return res
        

    def peek(self) -> int:
        n = len(self.input) -1
        for i in range(n):
            self.output.append(self.input.pop())
        res = self.input[0]
        for i in range(n):
            self.input.append(self.output.pop())
        return res
        

    def empty(self) -> bool:
        return True if len(self.output) == 0 and len(self.input) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# BRUTE FORCE APPROACH

# IMPLEMENTATION OF QUEUE USING STACKS

# Create two stacks.
# Before you push to the first stack, move all the element on the 1st stack to the second, and send all the elements from second to the first. 

# OPTIMAL APPROACH
# We only move all content to output once pop() operation.
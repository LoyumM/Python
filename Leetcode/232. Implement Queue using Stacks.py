class MyQueue:

    def __init__(self):
        # Initialize two stacks
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # Push element onto stack_in
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure stack_out has the current elements to pop from
        self._transfer()
        # Pop the element from stack_out
        return self.stack_out.pop()

    def peek(self) -> int:
        # Ensure stack_out has the current elements to peek from
        self._transfer()
        # Peek the element from stack_out
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Queue is empty if both stacks are empty
        return not self.stack_in and not self.stack_out

    def _transfer(self) -> None:
        # Transfer elements from stack_in to stack_out if stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
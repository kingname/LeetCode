"""
https://leetcode.com/submissions/detail/147676630/


Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.


push(x) -- Push element x onto stack.


pop() -- Removes the element on top of the stack.


top() -- Get the top element.


getMin() -- Retrieve the minimum element in the stack.




Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_value = None
        self.queue = []
        self.min_list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        if self.min_value is None:
            self.min_value = x
        else:
            if x <= self.min_value:
                self.min_list.append(self.min_value)
                self.min_value = x

    def pop(self):
        """
        :rtype: void
        """
        if self.queue:
            top_value = self.queue.pop(-1)
            if top_value == self.min_value:
                if self.min_list:
                    self.min_value = self.min_list.pop(-1)
                else:
                    self.min_value = None

    def top(self):
        """
        :rtype: int
        """
        if self.queue:
            return self.queue[-1]
        return None


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_value
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
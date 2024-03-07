class Node:
    def __init__(self, val = -1):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.size = 0
        self.dummy_start = Node()
        self.dummy_end = Node()
        self.dummy_start.next = self.dummy_end
        self.dummy_end.prev = self.dummy_start

    def append(self, node) -> Node:
        left, right = self.dummy_end.prev, self.dummy_end
        node.next = right
        node.prev = left
        left.next = node
        right.prev = node
        self.size += 1
        
        return node

    def popLeft(self) -> bool:
        if self.size == 0: return False
        firstNode = self.dummy_start.next
        self.dummy_start.next = firstNode.next
        firstNode.next.prev = self.dummy_start
        del firstNode
        self.size -= 1
        return True

    def peekLeft(self) -> Node:
        return self.dummy_start.next

    def peekRight(self) -> Node:
        return self.dummy_end.prev
    
    def getSize(self) -> int:
        return self.size

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxSize = k
        self.q = DLL()
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False 
        self.q.append(Node(value))
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        return self.q.popLeft()

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        print(self.q.dummy_start.next, self.q.dummy_end.prev)
        return self.q.peekLeft().val

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.q.peekRight().val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.q.getSize() == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.maxSize == self.q.getSize()


class MyCircularQueue2:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [0]*k
        self.head = self.tail = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull(): return False 
        self.data[self.tail % len(self.data)] = value
        self.tail += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty(): return False 
        self.head += 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty(): return -1
        return self.data[self.head % len(self.data)]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty(): return -1
        return self.data[(self.tail-1) % len(self.data)]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == self.tail

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.tail - self.head == len(self.data)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
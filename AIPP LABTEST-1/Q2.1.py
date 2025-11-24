class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self._data.pop(0)

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({self._data})"
def test_queue():
    print("=== Test 1: Basic enqueue/dequeue ===")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue after enqueues:", q)
    print("Dequeued:", q.dequeue())
    print("Peek:", q.peek())
    print("Queue now:", q)
    print()

    print("=== Test 2: Dequeue all elements ===")
    while not q.is_empty():
        print("Dequeued:", q.dequeue())
    print("Queue empty:", q.is_empty())
    print()

    print("=== Test 3: Peek on empty queue ===")
    q2 = Queue()
    print("Peek result:", q2.peek())   # Should be None
    print()

    print("=== Test 4: Error handling on empty dequeue ===")
    try:
        q2.dequeue()
    except IndexError as e:
        print("Caught expected error:", e)
    print()

    print("=== Test 5: Mixed operations ===")
    q3 = Queue()
    for i in range(5):
        q3.enqueue(i)
    print("Queue:", q3)
    print("Dequeued:", q3.dequeue())
    q3.enqueue(99)
    print("Queue after mixed operations:", q3)


# Run tests
test_queue()

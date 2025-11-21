# ================================================================
# PART 2: Elementary Data Structures Implementation
# ================================================================

# ------------------------------------------------
# 1. ARRAY IMPLEMENTATION
# ------------------------------------------------

class MyArray:
    def __init__(self):
        self.data = []

    def insert(self, index, value):
        """Insert value at a given index."""
        if index < 0 or index > len(self.data):
            raise IndexError("Index out of bounds")
        self.data.insert(index, value)

    def append(self, value):
        """Append value at the end."""
        self.data.append(value)

    def delete(self, index):
        """Delete element at index."""
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data.pop(index)

    def get(self, index):
        """Access element at index."""
        if index < 0 or index >= len(self.data):
            raise IndexError("Index out of bounds")
        return self.data[index]

    def __str__(self):
        return str(self.data)


# ------------------------------------------------
# 2. MATRIX (2D ARRAY)
# ------------------------------------------------

class Matrix:
    def __init__(self, rows, cols, default=0):
        self.rows = rows
        self.cols = cols
        self.matrix = [[default for _ in range(cols)] for _ in range(rows)]

    def set(self, r, c, value):
        """Set matrix[r][c] = value"""
        self.matrix[r][c] = value

    def get(self, r, c):
        """Return matrix[r][c]"""
        return self.matrix[r][c]

    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)


# ------------------------------------------------
# 3. STACK IMPLEMENTATION (ARRAY-BASED)
# ------------------------------------------------

class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.data:
            raise IndexError("Stack underflow")
        return self.data.pop()

    def peek(self):
        if not self.data:
            raise IndexError("Stack empty")
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)


# ------------------------------------------------
# 4. QUEUE IMPLEMENTATION (ARRAY-BASED WITH POINTER)
# ------------------------------------------------

class Queue:
    def __init__(self):
        self.data = []
        self.front_index = 0  # Avoids O(n) pop(0)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow")
        value = self.data[self.front_index]
        self.front_index += 1
        return value

    def front(self):
        if self.is_empty():
            raise IndexError("Queue empty")
        return self.data[self.front_index]

    def is_empty(self):
        return self.front_index >= len(self.data)

    def __str__(self):
        return str(self.data[self.front_index:])


# ------------------------------------------------
# 5. SINGLY LINKED LIST IMPLEMENTATION
# ------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new

    def insert_at_end(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def delete_value(self, value):
        if not self.head:
            return
        if self.head.value == value:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.value != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def traverse(self):
        """Return list of all values."""
        values = []
        curr = self.head
        while curr:
            values.append(curr.value)
            curr = curr.next
        return values


# ------------------------------------------------
# 6. OPTIONAL ROOTED TREE USING LINKED NODES
# ------------------------------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self, level=0):
        """Print tree structure (indentation shows hierarchy)."""
        print("  " * level + str(self.value))
        for child in self.children:
            child.traverse(level + 1)


# ------------------------------------------------
# TESTING ALL IMPLEMENTATIONS
# ------------------------------------------------

def run_tests():
    print("============== ARRAY TEST ==============")
    arr = MyArray()
    arr.append(10)
    arr.append(20)
    arr.insert(1, 15)
    arr.delete(0)
    print("Array:", arr)

    print("\n============== MATRIX TEST ==============")
    mat = Matrix(2, 3)
    mat.set(0, 1, 5)
    print(mat)

    print("\n============== STACK TEST ==============")
    st = Stack()
    st.push(5)
    st.push(10)
    st.push(15)
    print("Stack:", st)
    print("Popped:", st.pop())

    print("\n============== QUEUE TEST ==============")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Queue:", q)
    print("Dequeue:", q.dequeue())
    print("Queue After:", q)

    print("\n============== LINKED LIST TEST ==============")
    ll = LinkedList()
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_end(4)
    ll.delete_value(2)
    print("Linked list:", ll.traverse())

    print("\n============== ROOTED TREE TEST ==============")
    root = TreeNode("Root")
    child1 = TreeNode("Child A")
    child2 = TreeNode("Child B")
    child1.add_child(TreeNode("A1"))
    child1.add_child(TreeNode("A2"))
    child2.add_child(TreeNode("B1"))
    root.add_child(child1)
    root.add_child(child2)
    root.traverse()


if __name__ == "__main__":
    run_tests()

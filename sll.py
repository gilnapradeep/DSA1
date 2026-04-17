class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self, values):
        self.head = None
        if values:
            for val in values:
                self.append(val)
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def insert_pos(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < pos - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node
    def insert_after_node(self, key, data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == key:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Node not found")
    def insert_before_node(self, key, data):
        new_node = Node(data)
        if self.head is None:
            print("list is empty")
            return
        if self.head.data == key:
            new_node.next = self.head
            self.head = new_node
            return 
        prev = None
        current = self.head
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("Node not found")
            return
        new_node.next = current
        prev.next = new_node
    def delete_begin(self):
        if not self.head:
            print("List empty")
            return
        self.head = self.head.next
    def delete_end(self):
        if not self.head:
            print("list empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    def delete_pos(self, pos):
        if not self.head:
            print("list empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        current = self.head
        count = 0
        while current.next and count < pos - 1:
            current = current.next
            count += 1
        if not current.next:
            print("position out of range")
            return
        current.next = current.next.next
    def delete_by_value(self, key):
        if self.head is None:
            print("list empty")
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        prev = None
        current = self.head
        while current and current.data != key:
            prev = current
            current = current.next
        if current is None:
            print("value not found")
            return
        prev.next = current.next
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def duplicates(self):
        seen = set()
        prev = None
        current = self.head
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next
    def delete_occurances(self):
        if not self.head:
            return
        freq = {}   # 1, 2, 3, 2, 4, 1
        current = self.head
        while current:
            freq[current.data] = freq.get(current.data, 0) + 1
            current = current.next
        dummy = Node(0)    
        dummy.next = self.head    # dummy -> 1 -> 2 -> 3 -> 2 -> 4 -> 1
        prev = dummy
        current = self.head
        while current:
            if freq[current.data] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        self.head = dummy.next
    def middle(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    def mid(self):
        if not self.head:
            return None
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        mid = count // 2
        current = self.head
        for _ in range(mid):
            current = current.next
        return current.data
    def delete_mid(self):
        if not self.head or not self.head .next:
            self.head = None
            return
        slow = self.head
        fast = self.head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
    def merge_lists(self, other):
        if not self.head:
            self.head = other.head
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other.head
        return self
    def cycle(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow== fast:
                return True
        return False
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "->".join(result)
ll = LinkedList([10,20,10,30,20])
print("initial list")
print(ll)
ll.insert_begin(5)
print("insert begin")
print(ll)
ll.insert_end(35)
print("insert end")
print(ll)
ll.insert_pos(15,2)
print("insert position")
print(ll)
ll.insert_after_node(20, 5)
print("insert after node")
print(ll)
ll.insert_before_node(5,10)
print("insert before node")
print(ll)
ll.delete_begin()
print("delete begin")
print(ll)
ll.delete_end()
print("delete end")
print(ll)
ll.delete_pos(1)
print("delete pos")
print(ll)
ll.delete_by_value(10)
print("delete by value")
print(ll)
ll.reverse()
print("reverse")
print(ll)
ll.duplicates()
print("duplicates")
print(ll)
ll.delete_occurances()
print("delete occurances")
print(ll)
# ll.middle()
print("middle")
print(ll.middle())
# ll.mid()
print("middle without fast pointer")
print(ll.mid())
ll.delete_mid()
print("delete mid")
print(ll)

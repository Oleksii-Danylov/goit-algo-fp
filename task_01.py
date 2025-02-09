'''
Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.'''


from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Optional["Node"] = None

class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_end(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None  

        left = self._merge_sort(head)
        right = self._merge_sort(next_to_middle)

        return self._merge(left, right)

    def _get_middle(self, head):
        if head is None:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def _merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self._merge(left.next, right)
        else:
            result = right
            result.next = self._merge(left, right.next)

        return result

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" , ")
            cur = cur.next
        print("None")

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    a, b = list1.head, list2.head

    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a else b

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

llist = LinkedList()
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(4)
llist.insert_at_end(2)

print("\nОригінальний список:")
llist.print_list()

llist.reverse()
print("\nРеверсований список:")
llist.print_list()

llist.merge_sort()
llist2 = LinkedList()
llist2.insert_at_end(5)
llist2.insert_at_end(6)
llist2.insert_at_end(7)

merged_list = merge_sorted_lists(llist, llist2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_circle(head):
    if not head:
        return False
    slow = head
    fast = head.next
    while fast and fast.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return  False

# Create a 5 nodes linked list with a circle
node = ListNode(1)
second_node = ListNode(2)
node.next = second_node
third_node = ListNode(3)
second_node.next = third_node
fourth_node = ListNode(4)
third_node.next = fourth_node
fifth_node = ListNode(5)
fourth_node.next = fifth_node
fifth_node.next = second_node

# Figure out the linked list has a circle or not
print(has_circle(node))
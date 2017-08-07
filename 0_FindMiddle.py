#find the middle element of linked list in one pass


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def find_middle1(Node):
    flag = False
    half_node = Node
    while Node:
        Node = Node.next
        if flag:
            half_node = half_node.next
        flag = not flag
    return "Middle node of the linked list is %s" % str(half_node)

def find_middle2(Node):
    List = []
    while Node:
        List.append(Node)
        Node = Node.next
    return "Middle node of the linked list is %s" % str(len(List)/2)


def find_middle3(Node):
    fast = Node
    slow = Node
    while fast:
        if fast.next:
            fast = fast.next.next
            slow = slow.next
        else:
            break
    return  "Middle node of the linked list is %s" % str(slow)


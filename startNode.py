# coding: utf-8

from node import Node
from chainedList import Chained_List

def test_print_node():
    n1 = Node(1)
    n2 = Node(5)
    n1.link = n2

    n3 = Node (6)
    n2.link = n3
    print(n1)

def print_recurs(param_node):
    print("print_rcurs"+ str(param_node.data))

    if param_node.link is not None:

        pointer = param_node.link
        print_recurs(pointer)


if __name__ == "__main__":
    # just a test to see how the __str__ method of node work's
    test_print_node()
    chained_list = Chained_List([1,5,6,12,34])

    chained_list.insert_node_after(5,9)
    chained_list.delete_node(1)
    print(chained_list.first_node)
    print_recurs(chained_list.first_node)

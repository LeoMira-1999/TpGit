# coding: utf-8

from node import Node

class Chained_List:
    """
    Chained list Object
    Parameters
    ----------
    nodes : list
        list that we want to transfert in a chained list of Node object
    """
    def __init__(self, nodes):
        self.first_node = Node(nodes[0])
        node = self.first_node
        i = 1
        while i < len(nodes):
            node.link = Node(nodes[i])
            node = node.link
            i += 1

    def insert_node_after(self, data, new_node):
        """
        insert a new node after the node with the value == data
        Parameters
        ----------
        data : searched data
        new_node : node to insert
        """
        current_node = self.first_node

        while current_node is not None:
            if current_node.data == data:
                break

            current_node = current_node.link

        new_node = Node(new_node)
        new_node.link = current_node.link
        current_node.link = new_node

    def delete_node(self, data):
        """
        delete all node(s) value == data
        Parameters
        ----------
        data : searched data to delete
        """
        if self.first_node.data == data:
            self.first_node = self.first_node.link

        current_node = self.first_node

        while current_node.link is not None:
            if current_node.link.data == data:
                current_node.link = current_node.link.link
            current_node = current_node.link

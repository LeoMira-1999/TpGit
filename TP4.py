# coding: utf-8

class Tree_Node:

    def __init__(self, parent_node):
        self.parent_node = parent_node
        self.link_L = None
        self.link_R = None

    def __str__(self): #permet la lecture en profondeur
        if self.is_leaf():
            return str(self.parent_node)
        else:
            return "["+str(self.link_L) +":"+ str(self.link_R) + "]" + str(self.parent_node)

    def print_Tree_Node(self):
        if self.link_L:
            self.link_L.print_Tree_Node()
        print(self.parent_node)

        if self.link_R:
            self.link_R.print_Tree_Node()

    def is_leaf(self):
        return self.link_L is None and self.link_R is None

    def delete_node(self, target_node):
        if target_node < self.parent_node:
            self.link_L.delete_node(target_node)
        elif target_node > self.parent_node:
            self.link_R.delete_node(target_node)
        elif target_node == self.parent_node:
            self.parent_node = None


    def add_node(self, parent_node): #FAIRE STR et INT
        if self.parent_node:
            if parent_node < self.parent_node:
                if self.link_L is None:
                    self.link_L = Tree_Node(parent_node)
                else:
                    self.link_L.add_node(parent_node)
            elif parent_node > self.parent_node:
                if self.link_R is None:
                    self.link_R = Tree_Node(parent_node)
                else:
                    self.link_R.add_node(parent_node)
        else:
            self.parent_node = parent_node

class Tree:

    def __init__(self, selfNode):
        self.selfNode = selfNode

    def transversal_deep(self): #permet de faire une vue en profondeur avec __str__ de Tree_Node
        print(self.selfNode)



#############################################################################
n1 = Tree_Node(10)

"""
n1.print_Tree_Node()

print(n2.is_leaf())

print(n1.is_leaf())
"""

arbre = Tree(n1)

arbre.transversal_deep()
n1.add_node(5)
n1.add_node(15)
n1.add_node(4)
n1.add_node(3)
n1.add_node(2)
arbre.transversal_deep()
n1.delete_node(2)
arbre.transversal_deep()

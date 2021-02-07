# coding: utf-8

import unittest
from linkedList import Node, LinkedList

class TestChainedList(unittest.TestCase):
    """
    Test the chained list class from the ChainedList library
    """


    def setUp(self):
        """Initialisation des tests"""
        self.chained_list = LinkedList(["a", "b", "c", "d", "e"])


    def test_created_pile_is_empty(self):
        """Test si pile cree est vide"""

        result = LinkedList([])
        self.assertIsNone(result.head)


    def test_piling_pile_not_empty(self):
        """Test si pile non vide lors d'empilage"""

        self.assertIsNotNone(self.chained_list)


    def test_pile_and_depile(self):
        """Test si empilage et depilage reviens a la meme pile"""

        prev_res = self.chained_list.entire_llist()
        self.chained_list.add_first(Node("t"))

        self.chained_list.remove_node("t")

        res = self.chained_list.entire_llist()

        self.assertEqual(prev_res, res)



    def test_piling_on_top(self):
        """Test si empilement de lambda est bien lambda qui est empile"""

        self.chained_list.add_first(Node("t"))

        self.assertEqual(str(self.chained_list.get(0)),"t")


if __name__ == '__main__':
    unittest.main()#chaque points est un test execute

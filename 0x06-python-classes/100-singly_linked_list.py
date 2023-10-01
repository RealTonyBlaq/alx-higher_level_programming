#!/usr/bin/python3
"""
Defining a class Node that represents the node of
a singly linked list
"""


class Node:
    """ Node of a singly linked list """

    def __init__(self, data, next_node=None):
        """
        Initializes the Node with two private instance attributes:

        args:
        -----

        data: An int
        next_node: Must be another class object(new node) or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Retrieves the data """
        return self.__data

    @data.setter
    def data(self, value):
        """ Sets data to value """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Retrieves the next_node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ sets the next_node to value """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


""" Defines a class SinglyLinkedList"""


class SinglyLinkedList:
    """ This class would insert the nodes into the list """

    def __init__(self):
        """ initializes the head list """
        self.head = None

    def __str__(self):
        """ Returns a string representation of the list which is printable """
        my_list = ""
        current = self.head
        while current:
            my_list += str(current.data)
            if current.next_node:
                my_list += "\n"
            current = current.next_node
        return my_list

    def sorted_insert(self, value):
        """
        A public instance method that sorts the list in
        ascending order and then inserts a new node

        """
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
        elif self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            prev = None
            current = self.head
            while current and current.data < value:
                prev = current
                current = current.next_node
            prev.next_node = new_node
            new_node.next_node = current

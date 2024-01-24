#!/use/bin/python3
"""Defines a node of a singly linked list. """


class Node:
    """Represent the node of a singly linked list. """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with the provided data and next_node.

        Args:
            data (int): The data for the node.
            next_node (Node, optional): The next node in the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data of the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next node in the list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the list.

        Raises:
            TypeError: If next_node is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list.

    Attributes:
        __head: Private instance attribute representing the head of the list.
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value for the new Node.
        """
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the entire list."""
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()

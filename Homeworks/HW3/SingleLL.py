# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu


from queue import Empty


class SingleLinkedList:
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""

        __slots__ = "_element", "_next"  # streamline memory usage

        def __init__(self, element, next):  # initialize node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to next node

    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the linkedlist."""
        return self._size

    def is_empty(self):
        """Return True if the linkedlist is empty."""
        return self._size == 0

    def top(self):
        """Return (but do not remove) the element at the top of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty("list is empty")
        return self._head._element  # head of list

    def insert_from_head(self, e):
        """Add element e to the head of the linkedlist."""
        # Create a new link node and link it
        new_node = self._Node(e, self._head)
        self._head = new_node
        self._size += 1

    def delete_from_head(self):
        """Remove and return the element from the head of the linkedlist.

        Raise Empty exception if the linkedlist is empty.
        """
        if self.is_empty():
            raise Empty("list is empty")
        to_return = self._head._element
        self._head = self._head._next
        self._size -= 1
        return to_return

    def __str__(self):
        result = []
        curNode = self._head
        while curNode is not None:
            result.append(str(curNode._element) + "-->")
            curNode = curNode._next
        result.append("None")
        return "".join(result)

    def remove_all_occurance(self, value):
        """
        @value: the value we are trying to remove from the self list.
        remove any node that contains value in self linked list. Return nothing.
        Example:
        l1: 5 --> 4 --> 2 --> 4 --> 1 --> 9 --> 4 --> None
        >>> l1.remove_all_occurance(4)
        l1 should become: 5 --> 2 --> 1 --> 9 --> None
        @return: Nothing
        """
        # TODO: Problem 1
        # Initialize current and previous pointers
        curNode = self._head
        prevNode = None

        # Traverse the SLL
        while curNode:
            # If curNode needs to be deleted, no need to change prevNode
            if curNode._element == value:
                # If curNode is the head, change the head pointer
                if prevNode is None:
                    self._head = curNode._next
                # If curNode is not the head, change the prevNode pointer
                else:
                    prevNode._next = curNode._next
                self._size -= 1
            # If no need to delete curNode, change the prevNode to be curNode
            else:
                prevNode = curNode
            curNode = curNode._next

    def reverse(self):
        """
        reverses self list.
        Example:
        1 --> 2 --> 3 --> 4 --> None
        >>> l.reverse()
        4 --> 3 --> 2 --> 1 --> None
        @return: Nothing
        """
        # TODO: Problem 2
        # Initialize current and previous pointers
        curNode = self._head
        prevNode = None

        # Traverse the SLL
        while curNode:
            nextNode = curNode._next  # Store next node
            curNode._next = prevNode  # Change ref
            prevNode = curNode  # Update prevNode
            curNode = nextNode  # Update curNode

        # Set head to the last node
        self._head = prevNode

    def sublist(self, otherlist):
        """
        @otherlist: class SingleLinkedList.
        Return True if otherlist is sublist of self. Return False otherwise.
        (Definition of sublist: A list that makes up part of a larger list)

        Example:
        self list(l1):
        1 --> 2 --> 3 --> 4 --> None
        otherlist:
        None; 1 --> None; 1 --> 2 --> None; 1 --> 2 --> 3 --> None;
        1 --> 2 --> 3 --> 4 --> None; 2 --> None; 2 --> 3 --> None;
        2 --> 3 --> 4 --> None; 3 --> None; 3 --> 4 --> None; 4 --> None
        Are valid sublists. Should return True for any of the above cases.
        >>> l1.sublist(otherlist)
        True

        otherlist:
        1 --> 1 --> None
        >>> l1.sublist(otherlist)
        False

        @return: True or False
        """
        # TODO: Problem 3
        # Empty list is a sublist
        if otherlist.is_empty():
            return True

        # Traverse the self SLL to find the startNode for comparison
        startNode = self._head
        while startNode:
            self_curNode = startNode
            other_curNode = otherlist._head

            # If one valid startNode is found, traverse two SLL's to compare
            while self_curNode._element == other_curNode._element:
                self_curNode = self_curNode._next
                other_curNode = other_curNode._next
                # If the end of otherlist is reached, it is a sublist
                if other_curNode is None:
                    return True
                # If the end of otherlist is not reached, but the end of self is reached, then otherlist must not be a sublist
                if self_curNode is None:
                    return False

            startNode = startNode._next

        # startNode not found, or no valid sublist found for every startNode
        return False


# def main():
#     print("-----------Testing remove_all_occurance-------------")
#     l1 = SingleLinkedList()
#     for i in range(10):
#         l1.insert_from_head(6)
#     print(l1)  # 6-->6-->6-->6-->6-->6-->6-->6-->6-->6-->None
#     l1.remove_all_occurance(6)
#     print(l1, "Expected: None")
#     print()

#     l1 = SingleLinkedList()
#     for i in range(10):
#         l1.insert_from_head(i % 2)
#     print(l1)  # 1-->0-->1-->0-->1-->0-->1-->0-->1-->0-->None
#     l1.remove_all_occurance(0)
#     print(l1, "Expected: 1-->1-->1-->1-->1-->None")
#     print()

#     print("-----------Testing reverse-------------")
#     l1 = SingleLinkedList()
#     for i in range(10):
#         l1.insert_from_head(i)
#     print(l1)  # 9-->8-->7-->6-->5-->4-->3-->2-->1-->0-->None
#     l1.reverse()
#     print(l1, "Expected: 0-->1-->2-->3-->4-->5-->6-->7-->8-->9-->None")

#     print("-----------Testing sublist-------------")
#     l1 = SingleLinkedList()
#     l2 = SingleLinkedList()
#     for i in range(10):
#         l1.insert_from_head(i)
#     for i in range(5):
#         l2.insert_from_head(i + 3)
#     print(l1)
#     print(l2)
#     print("Is l2 sublist of l1? Your answer:", l1.sublist(l2), ", Expected: True")


# if __name__ == "__main__":
#     main()

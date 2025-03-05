"""
Copyright 2023, University of Freiburg.
Chair of Algorithms and Data Structures.
Authors: Hannah Bast <bast@cs.uni-freiburg.de>
         Niklas Schnelle <schnelle@cs.uni-freiburg.de>
         Patrick Brosi <brosi@cs.uni-freiburg.de>

Bearbeitet von Lotta Frey
"""
from typing import List, Tuple, Any


class PriorityQueue:
    """ A priority queue, as explained in Vorlesung 9 """

    def __init__(self):
        self.items = [None]

    def __repr__(self):
        """ A priority queue in human-readable form. """
        return str(self.items)

    def size(self) -> int:
        """ The number of items in the PQ.

        >>> pq = PriorityQueue()
        >>> pq.size()
        0
        """
        return len(self.items) - 1

    def delete_min(self):
        """
        Delete minimum item from the heap while ensuring the heap property.

        >>> pq = PriorityQueue()
        >>> pq.insert(PriorityQueueItem(3, "Q"))
        >>> pq.insert(PriorityQueueItem(7, "B"))
        >>> pq.insert(PriorityQueueItem(2, "C"))
        >>> pq.insert(PriorityQueueItem(1, "X"))
        >>> pq.delete_min()
        >>> pq
        [None, 2C@1, 7B@2, 3Q@3]
        >>> pq.delete_min()
        >>> pq
        [None, 3Q@1, 7B@2]
        >>> pq.delete_min()
        >>> pq
        [None, 7B@1]
        >>> pq.delete_min()
        >>> pq
        [None]
        >>> pq.delete_min()
        >>> pq
        [None]
        """
        self.items[1] = self.items[len(self.items) - 1]
        self.items.pop(len(self.items) - 1)
        self.repair_heap_downwards(1)

    def get_min(self) -> 'PriorityQueueItem':
        """ Get item with minimal key.

        >>> pq = PriorityQueue()
        >>> pq.insert(PriorityQueueItem(3, "Q"))
        >>> pq.insert(PriorityQueueItem(7, "B"))
        >>> pq.insert(PriorityQueueItem(2, "C"))
        >>> pq.insert(PriorityQueueItem(1, "X"))
        >>> pq.get_min()
        1X@1
        >>> pq = PriorityQueue()
        >>> pq.get_min() is None
        True
        """
        if self.size() == 0:
            return None
        return self.items[1]

    def insert(self, item: 'PriorityQueueItem'):
        """
        Insert given item (create with PriorityQueueItem below).

        >>> pq = PriorityQueue()
        >>> pq
        [None]
        >>> pq.insert(PriorityQueueItem(3, "Q"))
        >>> pq
        [None, 3Q@1]
        >>> pq.insert(PriorityQueueItem(7, "B"))
        >>> pq
        [None, 3Q@1, 7B@2]
        >>> pq.insert(PriorityQueueItem(2, "C"))
        >>> pq
        [None, 2C@1, 7B@2, 3Q@3]
        >>> pq.insert(PriorityQueueItem(1, "X"))
        >>> pq
        [None, 1X@1, 2C@2, 3Q@3, 7B@4]
        """
        self.items.append(item)
        item.heap_index = len(self.items) - 1
        self.repair_heap_upwards(item.heap_index)

    def repair_heap_upwards(self, i: int):
        """
        Repair heap upwards, starting from the given position.

        """
        while i > 1:
            pi = i // 2
            if self.items[i].key < self.items[pi].key:
                self.swap_items(i, pi)
            else:
                break
            i = pi

    def repair_heap_downwards(self, i: int):
        """
        Repairs the heap property at node i against its children as described
        in the lecture

        >>> pq = PriorityQueue()
        >>> pq.items = [None,
        ...             PriorityQueueItem(7, "B", 1),
        ...             PriorityQueueItem(2, "C", 2),
        ...             PriorityQueueItem(3, "Q", 3)]
        >>> pq.repair_heap_downwards(1)
        >>> pq.items
        [None, 2C@1, 7B@2, 3Q@3]
        >>> pq.items = [None,
        ...             PriorityQueueItem(7, "B", 1),
        ...             PriorityQueueItem(3, "C", 2),
        ...             PriorityQueueItem(5, "Q", 3),
        ...             PriorityQueueItem(2, "A", 4)]
        >>> pq.repair_heap_downwards(2)
        >>> pq.items
        [None, 7B@1, 2A@2, 5Q@3, 3C@4]
        >>> pq.items = [None,
        ...             PriorityQueueItem(7, "B", 1),
        ...             PriorityQueueItem(3, "C", 2),
        ...             PriorityQueueItem(5, "Q", 3),
        ...             PriorityQueueItem(2, "A", 4)]
        >>> pq.repair_heap_downwards(1)
        >>> pq.items
        [None, 3C@1, 2A@2, 5Q@3, 7B@4]
        >>> pq.items = [None,
        ...             PriorityQueueItem(7, "B", 1)]
        >>> pq.repair_heap_downwards(1)
        >>> pq.items
        [None, 7B@1]
        """

        while i < len(self.items) - 1:
            if i * 2 >= len(self.items):
                break
            elif i * 2 == len(self.items) - 1:
                ci = i * 2
            else:
                if self.items[i * 2].key < self.items[i * 2 + 1].key:
                    ci = i * 2
                else:
                    ci = i * 2 + 1
            
            if self.items[i].key > self.items[ci].key:
                self.swap_items(i, ci)
            else:
                break
            i = ci

    def swap_items(self, i: int, j: int):
        """ Swap the items at the given positions. """
        self.items[i], self.items[j] = self.items[j], self.items[i]
        self.items[i].heap_index = i
        self.items[j].heap_index = j

    def heapify(self, list: List[Tuple[Any, Any]] = []):
        """
        Fills the PriorityQueue from the given list list containing
        (key, value) pairs so that afterwards the PriorityQueue
        fullfills the heap property. Any existing items will be overwritten.

        The entire procedure should run in O(n) time where n is the length
        of the list being heapified.

        >>> pq = PriorityQueue()
        >>> pq
        [None]
        >>> pq.heapify([(7, 'B'), (2, 'C'), (3, 'Q')])
        >>> pq
        [None, 2C@1, 7B@2, 3Q@3]
        >>> pq.heapify([(5, 'A'), (1, 'B'), (2, 'C')])
        >>> pq
        [None, 1B@1, 5A@2, 2C@3]
        >>> pq.heapify([])
        >>> pq
        [None]
        """

        self.items = [None]

        i = 1
        for item in list:
            new_item = PriorityQueueItem(item[0], item[1], i)
            self.items.append(new_item)
            i += 1
        
        n = (len(self.items) - 1) // 2

        while n > 0:
            self.repair_heap_downwards(i)
            n -= 1


        """ self.items = [None]
        
        for item in list:
            key = item[0]
            value = item[1]
            self.insert(PriorityQueueItem(key, value)) """


class PriorityQueueItem:
    """ An item of a priority queue, with key and value. """

    def __init__(self, key: Any, value: Any, heap_index: int = None):
        self.key = key
        self.value = value
        self.heap_index = heap_index

    def __repr__(self):
        """
        A priority queue item in human-readable form. For example, show element
        with key 1 and value X at position 5 as 1X@5.
        """
        return "%d%s@%d" % (self.key, self.value, self.heap_index)
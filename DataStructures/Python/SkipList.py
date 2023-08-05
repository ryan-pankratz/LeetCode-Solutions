from typing import Optional, Any
from random import random
from math import inf, log, floor


class StaticStack:
    """
    A stack class that has a max number of spots (Static)
    """

    def __init__(self, size) -> None:
        self.size = size
        self.top = 0
        self.values = [None] * size

    def push(self, item: Any) -> None:
        if self.top < self.size:
            self.values[self.top] = item
            self.top += 1

    def pop(self) -> Any:
        if self.top > 0:
            temp = self.values[self.top - 1]
            self.values[self.top - 1] = None
            self.top -= 1
            return temp

    def isEmpty(self) -> bool:
        return self.top == 0


class Node:

    def __init__(self, val: float) -> None:
        self.val = val
        self.next = None
        self.down = None
        self.height = 1

    def setDown(self, n) -> None:
        self.height = n.height
        self.down = n
        self._incrementHeight()

    def decreaseHeight(self):
        curr = self
        while curr is not None:
            curr.height -= 1
            curr = curr.down

    def _incrementHeight(self):
        curr = self
        while curr is not None:
            curr.height += 1
            curr = curr.down


class Skiplist:

    def __init__(self) -> None:
        self.head = Node(-inf)
        level1Head = Node(-inf)
        self.tail = Node(inf)
        level1Tail = Node(inf)
        self.head.next = self.tail
        # Assign a bottom level
        # self.head.down = level1Head
        # self.tail.down = level1Tail
        self.head.setDown(level1Head)
        self.tail.setDown(level1Tail)
        # Assign the bottom next
        level1Head.next = level1Tail

        self.levels = 1
        self.length = 0

    def search(self, value: int) -> bool:
        """
        Searches for value in self.
        """
        return self._search(value).next.val == value

    def _search(self, value: int) -> Node:
        curr = self.head
        while curr.down is not None:
            curr = self._search_on_level(curr, value)
            curr = curr.down

        return self._search_on_level(curr, value)

    def _search_on_level(self, curr: Node, value: int) -> Node:
        while (curr.next is not None and curr.next.val < value):
            curr = curr.next
        return curr

    def erase(self, value: int) -> None:
        """
        Precondition: There is a node in self such that value = node.val
        """
        # if self.length > 2 and floor(log(self.length - 1, 2)) < self.levels:
        #     self._delete_top_level()

        s = StaticStack(self.levels)

        curr = self.head.down

        while curr.down is not None:
            if curr.next.val < value:
                prev = None
                while (curr.next.val < value):
                    prev = curr
                    curr = curr.next

                currTemp = curr.down.next
                if currTemp.next and currTemp.next.height != currTemp.height:
                    currTemp = prev.down.next  # Should be h - 1
                    num_at_height = 1

                    while currTemp.next.height == currTemp.height:
                        num_at_height += 1
                        currTemp = currTemp.next

                    if num_at_height >= 2:
                        # Raise currTemp
                        newNode = Node(currTemp.val)
                        newNode.setDown(currTemp)
                        prev.next = newNode
                        newNode.next = curr
                        prev = newNode

                    curr.decreaseHeight()
                    prev.next = curr.next
                    
                    if prev.next.val == value:
                        s.push(prev.next)

                elif curr.next.val == value:
                    s.push(curr.next)

            elif curr.next.val != inf:  # First drop
                currTemp = curr.down.next
                if currTemp.next and currTemp.next.height != currTemp.height:
                    currTemp = curr.next.down.next  # Should be h - 1
                    # Lower divider
                    curr.next.decreaseHeight()
                    curr.next = curr.next.next

                    if currTemp.next.height == currTemp.height:
                        # Raise currTemp
                        newNode = Node(currTemp.val)
                        newNode.setDown(currTemp)
                        newNode.next = curr.next
                        curr.next = newNode
                elif curr.next.val == value:
                    s.push(curr.next)

            curr = curr.down

        prev = None
        while (curr.next.val < value):
            prev = curr
            curr = curr.next

        if curr.next.val != value:
            return False
        elif curr.next.height == 1:
            curr.next = curr.next.next
        else:
            movedVal = curr.val
            curr.next.val = movedVal

            switchHeight = curr.next.height # For duplicate node values, make sure changing correct node

            prev.next = curr.next # cut out current

            while not s.isEmpty():
                curr = s.pop()
                if curr.height != switchHeight:
                    break # Switched Final one
                curr.val = movedVal
        self.length -= 1

        if self.head.down.down != None and self.head.down.next.val == inf: # Blank upper level
            self._delete_top_level()
        return True



    def add(self, value: int) -> None:
        curr = self.head

        # if floor(log(self.length + 1 , 2)) > self.levels:
        #     self._make_new_level()

        while curr.down is not None:
            curr = self._search_on_level(curr, value)

            tempCurr = curr.down.next
            height = tempCurr.height

            if tempCurr.next and tempCurr.next.next and tempCurr.next.height == height and tempCurr.next.next.height == height:  # Three in a row of same height
                newNode = Node(tempCurr.next.val)
                newNode.setDown(tempCurr.next)
                newNode.next = curr.next
                curr.next = newNode

                if newNode.height == self.levels + 1:
                    self._make_new_level()

            curr = curr.down

        curr = self._search_on_level(curr, value)

        newNode = Node(value)
        newNode.next = curr.next
        curr.next = newNode

        self.length += 1

    def _make_new_level(self):
        newHead = Node(-inf)
        newTail = Node(inf)
        newHead.setDown(self.head)
        newTail.setDown(self.tail)
        self.head = newHead
        self.tail = newTail
        self.head.next = self.tail
        self.levels += 1

    def _delete_top_level(self):
        self.head = self.head.down
        self.tail = self.tail.down
        self.head.decreaseHeight()
        self.tail.decreaseHeight()
        self.levels -= 1

    def coinflip(self):
        """
        Returns true if random() < 0.5, else returns false.
        """
        return random() < 0.5

    def printList(self):
        # f = open("test.txt", "a")
        i = 0
        while i < self.levels + 1:
            count = 0
            outStr = []
            curr = self.head
            j = 0
            while j < i:
                curr = curr.down
                j += 1
            while curr.next is not None:
                outStr.append(str(curr.val) + " -> ")
                count += 1
                curr = curr.next
            outStr.append(str(curr.val))
            count += 1
            count -= 2
            print(''.join(outStr))
            print(str(count))
            # f.write(''.join(outStr))
            # f.write(str(count) + "\n")
            i += 1
        # f.close()

    def toList(self) -> list[int]:
        curr = self.head
        while curr.down is not None:
            curr = curr.down

        lst = []
        curr = curr.next
        while curr.next is not None:
            lst.append(curr.val)
            curr = curr.next
        return lst

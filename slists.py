class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Slist:
    def __init__(self, val):
        node = Node(val)
        self.head = node

    def addNode(self, val):
        node = Node(val)
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = node

    def printAllValues(self, msg=""):
        runner = self.head
        if runner is None:
            return False
        print("\n\nhead points to ", id(self.head))
        print("Printing the values in the list ---", msg, "---")
        while runner.next:
            print(id(runner), runner.val, id(runner.next))
            runner = runner.next
        print(id(runner), runner.val, id(runner.next))

    def removeNode(self, val):
        runner = self.head
        if runner.val == val:
            self.head = runner.next

        while runner.next:
            prev = runner
            runner = runner.next
            if runner.val == val:
                prev.next = runner.next

        if runner.next is None:
            if runner.val == val:
                return False

    def insertNode(self, val, idx):
        node = Node(val)
        runner = self.head
        count = 0
        while runner.next:
            runner = runner.next
            count += 1
            if count == idx-1:
                break
        node.next = runner.next
        runner.next = node

    def reverse(self, head):
        runner = self.head
        prev = None

        while runner:
            temp = runner.next
            runner.next = prev
            prev = runner
            runner = temp
            print("runner:", runner)

        self.head = prev


print("\n\n\n\n================== START OF THE PROGRAM ================")
list = Slist(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.printAllValues("Attempt 1")
list.reverse(list)
list.printAllValues("Attempt 2")
list.insertNode(111, 2)
list.printAllValues("Attempt 3")
list.removeNode(9)  # removes 9, which is one of the middle nodes in the list
list.printAllValues("Attempt 4")
list.removeNode(5)  # removes 5, which is the first value in the list
list.printAllValues("Attempt 5")
list.removeNode(1)  # removes 1, which is the last node in the list
list.printAllValues("Attempt 6")
list.removeNode(111)
list.printAllValues("Attempt 7")
list.removeNode(7)
list.printAllValues("Attempt 8")

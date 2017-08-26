#Homework 5
#William O'Brochta

#As a disclaimer, I really have little idea about complexity for these classes or really for anything other
#than sorting methods...

class Node:
    #Initialize the node
    def __init__(self,value=None, next=None):
        #Check if the node is an integer
        if isinstance(value,int):
            self.value = value
            self.next = next
            #I had to put this here to get the revese function to work.
            #I think that's allowed in the homework requirements.
            self.helper = None
        else:
            self.value = None
            self.next = None
            print 'An integer is required.'
    def __str__(self):
        return str(self.value)

class LinkedList:
    #Initialize the list
    #This is O(1) because we are only doing one thing.
    def __init__(self,value):
        self.head = Node(value)
    
    #Calculate the length.
    #I think this would be O(n) (n is number of nodes) because you've got to loop through all the elements.
    def length(self):
        start = self.head
        counter=1
        #When there is a next as in self.head.next, continue the loop until none left.
        while 'next' in dir(start.next):
            counter+=1
            start = start.next
        print counter

    #Add a node to the end of the linked list.
    #This should be O(n+1) where n is the initial number of nodes plus the one added with this function.
    #This is because I loop through the entire list until the end and then add the node.
    def addNode(self,new_value):
        start = self.head
        #Loop through the linked list to the last element.
        while 'next' in dir(start.next):
            start=start.next
        #Put the new_value on the last element.
        else:
            start.next = Node(new_value)

    #Adding a node after a specific value. Here seems similar to the previous one except that
    #we go until we find the value to add the new_value after. However, then we have to fill
    #out the rest of the linked list, so it would still be O(n+1) for n=length of initial list.
    def addNodeAfter(self, new_value, after_node):
        if Node(new_value).value is not None:
            counter = 1
            start = self.head
            #This finds the location of the after_node and defines the new_value as the next in the list.
            while counter != after_node:
                counter +=1
                start = start.next
            #This just re-arranges the rest of the list.
            move_after = start.next
            start.next = Node(new_value)
            start.next.next = move_after
        else:
            return

    #addNodeBefore just calls addNodeAfter, so the worst case is that it has the same complexity as
    #addNodeAfter. If before_node is 1, then the complexity is only O(1), but that's not the worst case.
    def addNodeBefore(self, new_value, before_node):
        if before_node==1:
            self.head=Node(new_value,self.head)
        else:
            addNodeAfter(new_value, before_node-1)
    
    #Here again it should be O(n) since we loop over everything once.
    def removeNode(self,node_to_remove):
        if Node(node_to_remove).value is not None:
            #Least complex case if the node to remove is just the first one.
            if node_to_remove == 1:
                self.head = self.head.next
            #Set a counter and check each node until we arrive at the one to remove.
            #Then "jump" over that node by re-defining start as start=self.head.
            #Finally, fill in the rest of the linked list as before.
            else:
                counter = 1
                start = self.head
                while counter != node_to_remove:
                    counter +=1
                    start = start.next
                move_after = start.next
                counter = 1
                start = self.head
                while counter != node_to_remove-1:
                    counter +=1
                    start = start.next
                start.next = move_after
        else:
            return

    #This is likely O(n^2) because we have to go through the list and remove elements
    #and put them in the temporary node and then put everything back together.
    def removeNodesByValue(self,value):
        #Set-up a temporary node
        temp = Node(float("-inf"))
        temp.next = self.head
        start = temp
        #Set-up the next node of the temporary node.
        new = temp.next
        #While a next node exists, find where the next value is value.
        #Re-define start to skip over that value.
        while new:
            if new.value == value:
                start.next = new.next
            else:
                start = new
            new = new.next
        return temp.next

    #Reverse is complex, O(n!) I think, because it has to check each element and then move it, meaning
    #that the linked list gets reversed one element at a time or n!.
    def reverse(self):
        first_node = self.head
        #This is, of course, the best case where nothing happens.
        if self.head.next == None:
            pass
        #Otherwise, reference the helper assigned to each node from earlier.
        #It's just an index to put the nodes in reverse order.
        else:
            node = self.head
            while node.next != None:
                node.next.helper=node
                node = node.next
            self.head = node
            current_node = self.head
            while current_node !=None:
                current_node.next = current_node.helper
                current_node = current_node.helper

    #This should be complexity O(n) since we only go through and print for as many nodes are in the list.
    def __str__(self):
        lists = "%s" %self.head
        h = self.head
        while 'next' in dir(h.next):
            lists += ",%s" %(h.next)
            h=h.next
        return lists


#Creating a list to test the functionality.

mylist = LinkedList(3)
#list is now just 3

mylist.addNode(5)
mylist.addNode(6)
#list is now 3,5,6

mylist.length()
#and length is 3.

mylist.addNodeAfter(4,2)
#list is now 3,5,4,6

mylist.addNodeBefore(7,1)
#list is now 7,3,5,4,6

mylist.removeNode(2)
#list is now 7,5,4,6

mylist.addNode(8)
mylist.addNode(8)
#list is now 7,5,4,6,8,8

mylist.removeNodesByValue(8)
#list is now 7,5,4,6

mylist.reverse()
print mylist
#once you reverse the list, call print to see the list reversed. The output of reverse() just shows that
#the object is not an integer and it has a structure.


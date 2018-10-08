class node:
    def __init__(self, data=None):  # did not work if data was not set to None here
        self.data= data             # didn't work if this was set to None
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()    # creating  access to a new node to use

    def append(self, data):
        new_node = node(data)   # creating a new node
        now = self.head           # setting the start point
        while now.next!= None:    # stepping through the nodes to find the end
            now = now.next
        now.next = new_node        # adding the new data to the end of the list

    def length(self):
        now = self.head
        count = 0              #initialinging to counter
        while now.next!= None:     # checking if the is a next node
            count += 1           # adding 1 for each iteration that go by
            now = now.next
        return print(count)       # displaying the ccount as the length of the list

    def show(self):
        lst = []     # creating a empty list
        current_node = self.head        # setting the starting point for the nodes
        while current_node.next!= None:      # checking if there is a next node
            current_node = current_node.next       # setting current node to the next node.
            lst.append(current_node.data)           # adding the current node data to the list
        print(lst)                                  # printing the list

my_list = linked_list()   # created a new instance of a linked_list

my_list.append(12)
my_list.append('how')
my_list.length()
my_list.show()

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def print_forward(self, data):
        if self.head is None:
            print("Double_Linked list is empty")
            return
        itr = self.head
        double_linked_list = ""
        while itr:
            if itr.data == data:
                while itr.data:
                    double_linked_list += str(itr.data) + '-->'
                print(double_linked_list)
            itr = itr.next
    # This method prints list in forward direction. Use node.next

    def print_backward(self, data):
        pass
    # Print linked list in reverse direction. Use node.prev for this.

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        linked_list = ""
        while itr:
            linked_list += str(itr.data) + '-->'
            itr = itr.next
        print(linked_list)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    
    def array_to_linked_lists(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at(self, index, data):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        if index==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                self.insert_at(count,data_to_insert)
                break
            count += 1
            itr = itr.next
    
    def remove_by_value(self, data_to_remove):
        if self.head is None:
            return
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_to_remove:
                self.remove_at(count)
                break
            count += 1
            itr = itr.next

        

if __name__ == '__main__':
    double_linked_lists = DoubleLinkedList()
    # linked_lists.insert_at_beginning(5)
    # linked_lists.insert_at_beginning(89)
    # linked_lists.insert_at_end(79)
    # linked_lists.insert_at_end(1)
    # linked_lists.insert_at_end(9876)
    array = ['banana','mango','grapes','orange','pawpaw','pineapple','melon']
    array2 = []
    double_linked_lists.array_to_linked_lists(array)
    double_linked_lists.print()
    double_linked_lists.print_forward('grapes')

    # 
    # li
    # linked_lists.print_forward()

    # linked_lists.print()
    # linked_lists.remove_by_value('pineapple')
    # linked_lists.print()
    # print('Length of linked list: ',linked_lists.get_length())


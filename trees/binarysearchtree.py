import random

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, value):
        if self.data == value:
            return True
        
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
            
    def find_min(self):
        if self.data:
            if self.left is None:
                return self.data
            elif self.left is not None:
                return self.left.find_min()
        else:
            return
    
    def find_max(self):
        if self.data:
            if self.right is None:
                return self.data
            elif self.right is not None:
                return self.right.find_max()
        else:
            return
    
    def find_sum(self):
        sum = 0
        if self.data:
            sum += self.data 
        if self.left:
            sum += self.left.find_sum()
        if self.right:
            sum += self.right.find_sum()
        return sum
        

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    # countries = ["india","Pakistan","Germany","USA","China","India","UK","USA"]
    numbers = [random.randint(1,10**6) for _ in range(1,100)]
    numbers_tree = build_tree(numbers)
    # countries_tree = build_tree(countries)
    # print(countries_tree.in_order_traversal())
    # print(f'Is Nigeria is in the list: {countries_tree.search("Nigeria")}')
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(random.randint(1,10)))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.find_sum())


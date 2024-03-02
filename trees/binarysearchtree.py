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
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_sum(self):
        sum = self.data
        if self.left:
            sum += self.left.find_sum()
        if self.right:
            sum += self.right.find_sum()
        return sum

    # delete using min value
    def delete_with_min(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_with_min(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_with_min(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_with_min(min_val)
        return self
    
    # delete using max value
    def delete_with_max(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete_with_max(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete_with_max(value)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.left is None:
                return self.right
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete_with_max(max_val)
        return self
        
# Utilizing the BinarySearchTreeNode
def build_tree(elements):
    print(f"Building tree with these list {elements}")
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    # countries = ["india","Pakistan","Germany","USA","China","India","UK","USA"]
    # numbers = [random.randint(1,100) for _ in range(1,100)]
    numbers = [2,1,3,4,5,7,4]
    numbers_tree = build_tree(numbers)
    # countries_tree = build_tree(countries)
    # print(countries_tree.in_order_traversal())
    # print(f'Is Nigeria is in the list: {countries_tree.search("Nigeria")}')
    # number_to_delete_with_max = int(input("enter number you desire to delete with max function: "))
    number_to_delete_with_min = int(input("enter number you desire to delete with min function: "))
    # numbers_tree.delete_with_max(number_to_delete_with_max)
    numbers_tree.delete_with_min(number_to_delete_with_min)
    print(f"After deleting number {numbers_tree.in_order_traversal()}")
    print(numbers_tree.search(random.randint(1,100)))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.find_sum())
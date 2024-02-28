from collections import deque 
import random
import time
from datetime import datetime

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def peek(self):
        return self.buffer[0]
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def reverse_string(self, value):
        reversed = value[::-1]
        self.enqueue(reversed)
        return reversed

customers = ['Uche','Anthony','Jerry','Amara',
             'Miracle','Reuben','Emma','Vivian']

delicacies = ['rice/beans', 'beans/yam', 'eba/eguisi', 'fufu/white-soup',
              'sphagetti', 'semo/okro','rice/stew','beans/plantain']

price_list = {'rice/beans':2500, 'beans/yam':1500, 'eba/eguisi':2000,
              'fufu/white-soup':2000, 'sphagetti':1900, 'semo/okro':2000,
              'rice/stew':1800,'beans/plantain':1400}

order_management = Queue()
iterations = 0
max_iterations = 5

while iterations < max_iterations:
    selected_delicacy = random.choice(delicacies)
    order_management.enqueue({
        'name': random.choice(customers),
        'delicacy': selected_delicacy,
        'price': price_list[selected_delicacy],
        'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    iterations += 1
    time.sleep(1.5)
    print(order_management.dequeue())
    time.sleep(2)
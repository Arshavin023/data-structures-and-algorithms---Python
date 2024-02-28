from collections import deque 
import random
import time
from datetime import datetime
import threading

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

order_management = Queue()

def place_orders(orders):
    for order in orders:
        print(f"Placing order for {order}")
        order_management.enqueue(order)
        time.sleep(1)

def serve_orders():
    time.sleep(3)
    while not order_management.is_empty():
        order = order_management.dequeue()
        print(f"Now serving order: {order}")
        time.sleep(2)

customers = ['Uche','Anthony',
             'Jerry','Amara',
             'Miracle','Reuben','Emma','Vivian'
             ]

delicacies = ['rice/beans', 'beans/yam', 'eba/eguisi', 'fufu/white-soup',
              'sphagetti', 'semo/okro','rice/stew','beans/plantain']

price_list = {'rice/beans':2500, 'beans/yam':1500, 'eba/eguisi':2000,
              'fufu/white-soup':2000, 'sphagetti':1900, 'semo/okro':2000,
              'rice/stew':1800,'beans/plantain':1400}

order_list = []
for customer in customers:
    for delicacy in delicacies:
        order_list.append(
            {'name': customer,
            'delicacy': delicacy,
            'price': price_list[delicacy],
            'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        
if __name__ == '__main__':
    orders = order_list
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()
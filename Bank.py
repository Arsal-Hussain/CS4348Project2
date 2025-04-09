import threading
import time
from queue import Queue
import random

tellers = 3
customers = 50

bank_door = threading.Semaphore(2) # max two customers in bank door
bank_safe = threading.Semaphore(2) # max two tellers at the safe
manager = threading.Semaphore(1) # max 1 teller with manager
teller_ready = threading.Semaphore(0) # determines if teller is ready for next customer

teller_queue = Queue()
customer_queue = Queue()

numCustomerServed = 0
numCustomerServed_lock = threading.lock()



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

class Teller(threading.Thread):
    def __init__(self, tid):
        super().__init__()
        self.id = tid
        self.customerAvailability = threading.Semaphore(0) # availability once taking a customer
        self.customer = None
        self.transaction = None
    def run(self):
        global customer_served
        while True:
                print(f"Teller {self.id} [Teller {self.id}]: Ready for Customer")
                teller_queue.put(self)
                teller_ready.release()

                self.customerAvailability.acquire() # customer will go to teller

                if self.customer is None:
                        break
                print(f"Teller {self.id} [Customer {self.customer.id}]: What is the transaction?")
                self.transaction = self.customer.getTransaction()

                if self.transaction == "Withdraw":
                      print(f"Teller {self.id} [Teller {self.id}]: Go to Manager")
                      manager.acquire()
                      print(f"Teller {self.id} [Teller {self.id}]: Interact with Manager")
                      time.sleep(random.uniform(0.005, 0.03))
                      print(f"Teller {self.id} [Teller {self.id}]: Manager complete")
                      manager.release()
                print(f"Teller {self.id} [Teller {self.id}]: Going to Safe")
                bank_safe.acquire()
                print(f"Teller {self.id} [Teller {self.id}]: In the Safe")
                time.sleep(random.uniform(0.01, 0.05))
                print(f"Teller {self.id} [Teller {self.id}]: Done in safe")
                bank_safe.release()

                print(f"Teller {self.id} [Customer {self.customer.id}]: Transaction Complete")
                self.customer.complete.release()

                self.customer.leave.acquire()

                with customerServed_lock:
                      numCustomerServed += 1
                      if numCustomerServed >= numCustomerServed:
                            break
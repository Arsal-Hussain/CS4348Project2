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
lock = threading.Lock()

teller_queue = Queue()
customer_queue = Queue()

numCustomerServed = 0
numCustomerServed_lock = threading.Lock()

class Teller(threading.Thread):
    def __init__(self, tid):
        super().__init__()
        self.id = tid
        self.customerAvailability = threading.Semaphore(0) # availability once taking a customer
        self.customer = None
        self.transaction = None
    def run(self):
        global numCustomerServed
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

                with numCustomerServed_lock:
                      numCustomerServed += 1
                      if numCustomerServed >= customers:
                            break

class Customer(threading.Thread):
    def __init__(self, cid):
        super().__init__()
        self.id = cid
        self.transaction = random.choice(["Deposit", "Withdraw"])
        self.complete = threading.Semaphore(0)
        self.leave = threading.Semaphore(0)

    def getTransaction(self):
        print(f"Customer {self.id} [Teller {self.teller.id}]: gives transaction")
        return self.transaction
    
    def run(self):
        time.sleep(random.uniform(0, 0.1))
        bank_door.acquire()
        print(f"Customer {self.id} [Customer {self.id}]: enters bank")

        teller_ready.acquire()
        teller = teller_queue.get()
        self.teller = teller
        teller.customer = self
        print(f"Customer {self.id} [Teller {teller.id}]: selects teller")
        teller.customerAvailability.release()

        self.complete.acquire()
        print(f"Customer {self.id} [Teller {teller.id}]: leaving bank")
        self.leave.release()
        bank_door.release()

tellers_thread = [Teller(i) for i in range(tellers)]
customers_thread = [Customer(i) for i in range(customers)]

for t in tellers_thread:
    t.start()
for c in customers_thread:
    c.start()
for c in customers_thread:
    c.join()

for t in tellers_thread:
    t.customer = None
    t.customerAvailability.release()

for t in tellers_thread:
    t.join()
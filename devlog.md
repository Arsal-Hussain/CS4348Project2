# April 8 10:46pm

Created git repository for Project 2, as usual instructions for project formats in this class.

# April 8 10:55pm

This will be a single application project, per the assignment. Within the single file will be classes for the Teller and Customer. They will use semaphores, as learned from class.

# April 8 10:58pm

Starting first session. Bank.py will be created to sync both sides of the project, the Customer and Teller, to eventually lead to an output. Will need to import threading module for python language and threading.Semaphore for sync. 

# April 8 11:08pm

Key components, there will be 3 tellers and 50 customers. Bank will be open when all three tellers are ready, otherwise customers cannot enter. A teller can only interact with a customer one at a time. When all 50 customers are served, the bank is closed.

# April 8 11:10pm

Teller will need to inform when they are ready to serve, should use queue to determine when the next customer is served. Threading semaphore will determine availability of tellers.

# April 8 11:24pm

Starting the Teller class. Each teller will have a unique id to identify themselves in the queue and semaphores for each customer interaction. This includes their individual availability and the transaction that will occur (withdrawal or deposit). If they enter the safe, this will need to be indicated. Using sleep to simulate the transaction time. Once the transaction is complete it will communicate to the current position of the Customer, and wait for their depature before opening availability.

# April 9 12:04am

Finished Teller class. Using queue to signal readiness. Waits for customer to meet teller using the Semaphore. Uses different transaction instances to define semaphore, such as withdrawal or meeting with the manager. Uses logging to track each action completed at bank.

# April 12 4:48pm

Working on new session. Most likely to do customer class. Each customer will be assigned a unique ID, random transaction type (either deposit or withdraw), and semaphores for when transaction is complete and when customer leaves.
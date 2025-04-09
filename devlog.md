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
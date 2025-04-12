# **CS 4348 Operating Systems Project 2**

## **Project Overview**
This project simulates the operation of a bank using Python's threading and semaphore modules. It models interactions between three tellers and fifty customers, coordinating access to shared resources like the safe, bank manager, and bank entrance.

The simulation enforces synchronization constraints and prints each thread’s activity following a strict logging format.

---

## **Files and Their Roles**
- **`Bank.py`** - The main simulation script containing all teller and customer thread logic.

---

## **How to Run the Program**
Ensure you're using **Python 3.10+** and run the following command:
```sh
python Bank.py
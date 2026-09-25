# System: Corporate Expense Tracker
# You are building an in-memory system to track corporate card 
# expenses. Implement the following methods. 
# You must maintain the state within your class.
# 
# Level 1: Core Operations
# Implement basic state management for users and expenses.
# add_user(user_id: str, name: str) -> bool: 
# Adds a new user. Returns True if successful, False if the user_id already exists.
# add_expense(expense_id: str, user_id: str, amount: int, merchant: str) -> bool: 
# Records an expense. Returns True if successful, False if the expense_id already exists OR 
# if the user_id does not exist.
# 
# Level 2: Analytics & Sorting Add the ability to retrieve and properly sort 

# expenses.get_user_expenses(user_id: str) -> list[str]: 
# Returns a list of strings formatted exactly as "<expense_id>: <merchant> - $<amount>".
# 
# Sorting rules: Sort the returned list by amount in descending order. 
# If amounts tie, sort by expense_id in ascending alphabetical order. 
# Return an empty list if the user does not exist or has no expenses.
# 
# Level 3: Limits & Constraints
# 
# Introduce spending limits and dynamic rejection 

# logic.set_user_limit(user_id: str, limit: int) -> bool: 
# Sets a maximum total spending limit for a user. Returns False if the user doesn't exist.
# 
# Modification to Level 1: Update add_expense. 
# If adding the new expense would push the user's total cumulative expenses strictly over their 
# assigned limit, reject the transaction (do not record it) and return False. 
# If a user has no limit set, they can spend infinitely.
# 
# Level 4: Auditing & SnapshotsImplement a system to back up and roll back the 
# database.create_snapshot(timestamp: int) -> None: 
# 
# Saves the complete state of all users, expenses, and limits at the given 
# timestamp.restore_snapshot(timestamp: int) -> bool: Restores the system to 
# the exact state it was in at timestamp. 
# Returns True if the snapshot exists, False otherwise.
# 
# Warning: Mutating the current state after a snapshot is taken must not alter the saved 
# snapshot.

import copy


class ExpenseTracker:
  def __init__(self):
    self.users = dict()
    self.expenses = dict() # maps expense id to the relevant user
    self.snapshots = dict()

  # Adds a new user. Returns True if successful, False if the user_id already 
  def add_user(self, user_id: str, name: str) -> bool:
    if user_id in self.users:
      return False
    self.users[user_id] = User(user_id, name)
    return True

  # Records an expense. Returns True if successful, False if the expense_id already exists OR 
  # if the user_id does not exist.
  def add_expense(self, expense_id: str, user_id: str, amount: int, merchant: str) -> bool: 
    if expense_id in self.expenses or user_id not in self.users:
      return False
    exp = Expense(expense_id, amount, merchant)
    usr = self.users[user_id]
    # insert into expenses table. 
    if usr.spend + amount > usr.limit:
      return False
    self.expenses[expense_id] = usr
    usr.expenses[expense_id] = exp
    usr.spend += amount
    return True

  def get_user_expenses(self, user_id: str) -> list[str]:
    if user_id not in self.users:
      return []
    
    usr = self.users[user_id]
    if not usr.expenses:
      return []
    
    # 1. Get a list of the Expense objects
    expenses_list = list(usr.expenses.values())
    
    # 2. Sort by -amount (descending) then id (ascending)
    expenses_list = sorted(key= lambda x: (-x.amount, x.id))    
    # 3. Format into strings
    return [f"{x.id}: {x.merchant} - ${x.amount}" for x in expenses_list]

  # Sets a maximum total spending limit for a user. Returns False if the user doesn't exist.
  def set_user_limit(self, user_id: str, limit: int) -> bool: 
    if user_id not in self.users:
      return False
    self.users[user_id].limit = limit
    return True

  def create_snapshot(self, timestamp: int) -> None:
    self.snapshots[timestamp] = {
      'users': copy.deepcopy(self.users),
      'expenses': copy.deepcopy(self.expenses)
    }

  # Restores the system to the exact state it was in at timestamp. 
  # Returns True if the snapshot exists, False otherwise.
  def restore_snapshot(self, timestamp: int) -> bool: 
    if timestamp not in self.snapshots:
      return False
      
    # Deep copy the snapshot back into the live variables.
    # We deepcopy again so the snapshot in storage isn't accidentally modified later!
    saved_state = self.snapshots[timestamp]
    self.users = copy.deepcopy(saved_state['users'])
    self.expenses = copy.deepcopy(saved_state['expenses'])
    return True

class Expense:
  def __init__(self, id : str, amount: int, merchant: str):
    self.id = id
    self.amount = amount
    self.merchant = merchant
    self.expenses = [] # we store the expenses as a list of expenses 

class User:
  def __init__(self, id : str, name : str):
    self.id = id
    self.name = name 
    self.expenses = dict() # maps id to expense
    self.limit = float('inf')
    self.spend = 0




# Sample Test Case 
# ExecutionPython

system = ExpenseTracker()

# # Level 1 & 2
system.add_user("u1", "Alice")               # Returns True
system.add_expense("e1", "u1", 50, "Uber")   # Returns True
system.add_expense("e2", "u1", 120, "Delta") # Returns True
system.add_expense("e3", "u1", 50, "Lyft")   # Returns True
# system.get_user_expenses("u1")               
# # Returns: ["e2: Delta - $120", "e1: Uber - $50", "e3: Lyft - $50"]

# # Level 3
# system.set_user_limit("u1", 250)             # Returns True (Current total: 220)
# system.add_expense("e4", "u1", 40, "Lunch")  # Returns False (220 + 40 > 250)

# # Level 4
# system.create_snapshot(100)
# system.add_user("u2", "Bob")                 # Returns True
# system.restore_snapshot(100)                 # Returns True
# system.add_expense("e5", "u2", 10, "Coffee") # Returns False ("u2" no longer exists)
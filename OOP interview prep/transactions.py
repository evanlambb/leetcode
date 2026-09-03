from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass

@dataclass
class Data:
    timestamp: str
    sender_id: str
    receiver_id: str
    amount: float
    currency: str
    trans_type: str

currencies = ["CAD", "USD"]

trans_types = ["deposit", "withdrawl", "premium"]

class DataChecker (ABC):

  @abstractmethod
  def execute(self):
    pass


class PipelineManager:
  def __init__(self):
    self.steps = []

  def add_step(self, step : DataChecker):
    self.steps.append(step)

  def run(self, batch: List[Data]) -> List[Data]:
        current_batch = batch
        # Hand the batch to the first step, take the result, 
        # and hand it to the next step.
        for step in self.steps:
            current_batch = step.execute(current_batch)
            
        return current_batch

  
# Need to verify that Timestamp, sender_id and receiver_id exist, amount is non-negative, and currency is in ["CAD", "USD"]
# trans_type is one of ["deposit", "withdrawl", "premium"]
class Validator(DataChecker):
  def execute(self, batch : List[Data]) -> List[Data]:
    new_batch = [] # List[Data]
    for data in batch:
      if data.timestamp and data.sender_id and data.receiver_id and data.amount >= 0 and data.currency in currencies and data.trans_type in trans_types:
        new_batch.append(data)
    return new_batch
# Need to check the velocity (no more than 10 large transfers in under a minute)
# flag transactions for more than $10k 
class Fraud(DataChecker):
    def execute(self, batch: List[Data]) -> List[Data]:
        clean_batch = []
        
        # Dictionary to store the sliding window of timestamps for each sender
        # Format: { "sender_id": [timestamp1, timestamp2, ...] }
        sender_history = {}

        for data in batch:
            # Check 1: Large Transfer Rule
            if data.amount > 10000:
                # Skip appending to clean_batch (effectively dropping it)
                continue 

            # Check 2: Velocity Rule (Sliding Window)
            sender = data.sender_id
            current_time = int(data.timestamp)

            # Initialize the list for a new sender
            if sender not in sender_history:
                sender_history[sender] = []

            # Append the current transaction's timestamp
            sender_history[sender].append(current_time)

            # Filter the list to only keep timestamps within the last 60 seconds
            sender_history[sender] = [
                t for t in sender_history[sender] 
                if current_time - t <= 60
            ]

            # If the sender has more than 10 transactions in this 60s window, flag it
            if len(sender_history[sender]) > 10:
                continue
                
            # If the transaction passes both checks, it is clean
            clean_batch.append(data)

        return clean_batch  
        



def main():
    # Using integers for timestamps to make the 60-second window math easy
    lst = [
        # 1. Valid transaction
        Data(1000, "alice", "bob", 500.0, "CAD", "deposit"),
        
        # 2. Fails Validation (Negative amount)
        Data(1005, "charlie", "bob", -50.0, "USD", "withdrawl"),
        
        # 3. Fails Validation (Invalid currency)
        Data(1010, "alice", "dave", 100.0, "EUR", "deposit"),
        
        # 4. Valid, but Fraud (> $10k)
        Data(1020, "eve", "bob", 15000.0, "USD", "premium"),
    ]
    
    # 5. Velocity Fraud (Alice does 11 transactions in 50 seconds)
    for i in range(11):
        lst.append(Data(1030 + i, "alice", "bob", 10.0, "CAD", "deposit"))
        
    pipeline = PipelineManager()
    pipeline.add_step(Validator())
    pipeline.add_step(Fraud())
    
    final_clean_data = pipeline.run(lst)
    print(f"Transactions that passed all checks: {len(final_clean_data)}")

if __name__ == "__main__":
    main()

from typing import List, Dict, Optional
from abc import ABC, abstractmethod
from dataclasses import dataclass


# Merchants on our platform don't just sell out of one garage anymore. They have inventory spread across multiple retail stores and warehouses. When a customer places an order, the backend system needs to figure out exactly which locations should ship which items, and then deduct that inventory.
# You need to build the FulfillmentEngine that processes an Order.
# Core Requirements:
# Inventory Management: You need a Location class that tracks its own inventory (how many of each product_id it currently holds).
# The Routing Logic: Your engine will receive an Order (a list of product IDs and requested quantities) and a list of available Location objects. It must return a FulfillmentPlan detailing exactly which location is fulfilling which items.
# Business Rules for Fulfillment:
# Rule 1 (Single-Origin Preference): The engine must first try to fulfill the entire order from a single location to save the merchant on shipping costs.
# Rule 2 (Split Fulfillment): If no single location has everything, the engine must split the order across multiple locations.
# State Mutation: Once a valid FulfillmentPlan is generated, the engine must deduct the reserved inventory from the respective Location objects.
# Edge Cases & Error Handling to Consider (Your interviewer will look for these):
# The Oversell (Transaction Safety): What happens if the customer orders 10 Red Shirts, but all locations combined only have 8? The system should raise a specific exception, but crucially, it must not deduct any inventory from the locations. (An order either entirely succeeds or entirely fails).
# Empty States: What happens if the order is empty, or the merchant has no locations set up?

class InsufficientStockError(Exception):
    """Raised when an order cannot be fully fulfilled from available inventory."""
    pass

@dataclass
class Order:
  items : dict[str, int] # maps the id to the quantity

class Location:
    def __init__(self, name: str, inventory: dict[str, int]): # maps the id to the quantity
        self.name = name
        self.inventory = inventory

    def remove_items(self, items_to_remove: dict[str, int]) -> None:
        for item, quantity in items_to_remove.items():
            self.inventory[item] -= quantity

    def can_fulfill(self, order: Order) -> bool:
        for item, quantity in order.items.items():
            if self.inventory.get(item, 0) < quantity:
                return False
        return True
# Is the plan for where we are going to source our items from 

# I want this to store the pairs of locations and what we are ordering from that location. Note that this may not be a complete order
class FulfillmentPlan:
  def __init__(self):
    self.plan: Dict[str, dict[str, int]] = {} # maps the location name to the items that we are getting from that location

  def add_location(self, location: Location, items: dict[str, int]) -> None:
    self.plan[location.name] = items

# This is the engine that generates the plan for us
class FulfillmentEngine:
    def __init__(self, locations: Optional[Dict[str, Location]] = None):
      self.locations = locations if locations is not None else {}

    def generate_plan(self, order: Order) -> Optional[FulfillmentPlan]:
      # Empty order is trivially fulfilled with an empty plan.
      if not order.items:
          return FulfillmentPlan()

      # No locations set up means we can't fulfill anything.
      if not self.locations:
          return None

      # Rule 1 (Single-Origin Preference): try to fulfill the whole order
      # from a single location to save on shipping.
      for location in self.locations.values():
          if location.can_fulfill(order):
              plan = FulfillmentPlan()
              plan.add_location(location, dict(order.items))
              return plan

      # Rule 2 (Split Fulfillment): draw from multiple locations, taking as
      # much of each remaining item as a location can provide.
      plan = FulfillmentPlan()
      remaining = dict(order.items)
      for location in self.locations.values():
          allocation: dict[str, int] = {}
          for item, quantity in remaining.items():
              take = min(quantity, location.inventory.get(item, 0))
              if take > 0:
                  allocation[item] = take
          if allocation:
              plan.add_location(location, allocation)
              # Deduct what this location covered from the remaining need.
              for item, take in allocation.items():
                  remaining[item] -= take
              remaining = {item: qty for item, qty in remaining.items() if qty > 0}
          if not remaining:
              break

      # The Oversell: if anything is still unmet, the order fails entirely
      # so no plan (and therefore no deduction) is produced.
      if remaining:
          return None
      return plan

    def fulfill_order(self, order: Order) -> bool:
        p = self.generate_plan(order)
        if p is None:
          # we do not have the inventory to complete the order
          raise InsufficientStockError("Cannot fulfill order: insufficient stock")
        # remove the inventory, as we have completed the order
        for location_name, items in p.plan.items():
            self.locations[location_name].remove_items(items)
        return True

    def add_location(self, location: Location) -> None:
      self.locations[location.name] = location




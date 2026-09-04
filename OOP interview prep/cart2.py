from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Building a cart using the decorator pattern. 
# 
# Must support:
# adding and removing products,
# calculating total BEFORE discounts
# A list of discounts applied and the exact dollar amount they 
#   reduced the price by (acting as contra-revenue for the accounting team).
# calculating total with discounts
# 
# Discounts to support:
# - Flat rate discounts     [DONE]
# - Percentage discounts    [DONE]
# - BOGO for the same product

@dataclass
class Item:
  id: str
  name: str
  quantity: int
  price: float
  discounts : float

@dataclass
class Ledger: 
  discounts: List[Discount]
  total_no_discounts : float
  total_with_discounts : float

@dataclass
class Discount:
  amount: float
  description: str

class CartComponent (ABC):
  @abstractmethod
  def calculate_total_with_discounts(self) -> float:
    pass

  @abstractmethod
  def calculate_total_no_discounts(self) -> float:
    pass

  @abstractmethod
  def add_discounts(self, ledger : Ledger):
    pass

class BaseCart (CartComponent):
  def __init__(self):
    self.items = []
  def calculate_total_with_discounts(self):
    total = 0
    for item in self.items:
      total += item.price * item.quantity
    return total
  def add_item(self, item : Item):
    self.items.append(item)
  def remove_item(self, item_id : str):
    for i in range(len(self.items)):
      if self.items[i].id == item_id:
        self.items.pop(i)
        return
  def calculate_total_no_discounts(self) -> float:
    return self.calculate_total_with_discounts()


  def add_discounts(self, ledger : Ledger):
    ledger.total_no_discounts = self.calculate_total_no_discounts()
    # There are no discounts to apply to the base class 
        
    
class DiscountDecorator(CartComponent):
  def __init__(self, cart_component : CartComponent):
    self.cart_component = cart_component

  def calculate_total_no_discounts(self) -> float:
    return self.cart_component.calculate_total_no_discounts()
    
class FlatDiscount (DiscountDecorator):
  def __init__(self, cart_component : CartComponent, flat_discount : float):
    super().__init__(cart_component)
    self.flat_discount = flat_discount

  def calculate_total_with_discounts(self):
    return max(self.cart_component.calculate_total_with_discounts() - self.flat_discount, 0.0)

  def add_discounts(self, ledger : Ledger):
    self.cart_component.add_discounts(leger)
    ledger.discounts.append(Discount(self.flat_discount, "Flat Discount"))
    ledger.total_with_discounts = ledger.total_with_discounts - self.flat_discount

class PercentDiscount (DiscountDecorator):
  def __init__(self, cart_component : CartComponent, percent_discount : float):
    super().__init__(cart_component)
    self.percent_discount = percent_discount

  def calculate_total_with_discounts(self):
    return self.cart_component.calculate_total_with_discounts() * (1-self.percent_discount)

  def add_discounts(self, ledger : Ledger):
    self.cart_component.add_discounts(leger)
    ledger.discounts.append(Discount(self.percent_discount * ledger.total_with_discounts, "Percent Discount"))
    ledger.total_with_discounts = ledger.total_with_discounts * (1-self.percent_discount)

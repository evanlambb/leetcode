from typing import List
from abc import ABC, abstractmethod
from dataclasses import dataclass
# I want to build a shopping cart OOP system to manage the price of a cart
# Must Support: 
# Discounts on specific items: e.g. item # 123 is $5 off
# Discounts on cart as a %
# Discounts on the shipping: e.g. potential for free shipping

# I think that this would be a good application of 
# the decorator pattern to wrap the cart in the discounts that need to be applied


@dataclass
class Item:
    id: str
    name: str
    price: float

# CartPricing will be our abstract partent class
class CartPricing (ABC):
    # get the current cart total, exclude the tax and shipping
    @abstractmethod
    def calculate_total(self) -> float:
        pass
    # return a list of all of the items in the cart
    @abstractmethod
    def get_items(self) -> List[Item]:
      pass
    # get the price of the cart including tax and shipping
    @abstractmethod
    def calculate_final_price(self) -> float: 
      pass
    
    @abstractmethod
    def get_shipping(self) -> float:
      pass

    def calculate_final_price(self) -> float: 
      return self.calculate_total() * 1.13 + self.get_shipping()
# BaseCart inherits from CartPricing, and is the default cart behaviour  
class BaseCart (CartPricing):
    def __init__(self, items : List[item], shipping : int):
        self.items = items
        self.shipping = shipping

    def calculate_total(self): # this then overrides the default behaviour of the CartPricing class. 
        total = 0
        for item in self.items:
            total += item.price
        print(total)
        return total
    def get_items(self) -> List[Item]:
        return self.items

    def calculate_final_price(self) -> float: 
        return self.calculate_total() * 1.13 + self.get_shipping()

    def get_shipping(self) -> float:
      return self.shipping

# CartDecorator inherits from CartPricing and is the "add ons" for the carts, highlighting discounts etc
class CartDecorator (CartPricing):
    def __init__(self, cart_pricing : CartPricing):
        self.cart_pricing = cart_pricing
    def get_items(self) -> List[Item]:
        return self.cart_pricing.get_items()

    def calculate_total(self): # this then overrides the default behaviour of the CartPricing class. 
        total = 0
        for item in self.items:
            total += item.price
        print(total)
        return total
    def get_shipping(self) -> float:
      return self.cart_pricing.get_shipping()

  

# CartDiscount inherits CartDecorator and takes a discount as a percentage (e.g. for 20% off, discount = 0.20)
class CartDiscount (CartDecorator):
    def __init__(self, cart_pricing : CartPricing, discount : float):
        self.cart_pricing = cart_pricing
        self.discount = discount
    def calculate_total(self):
        return self.cart_pricing.calculate_total() * (1- self.discount)
    

# ItemDiscount inherits CartDecorator
class ItemDiscount (CartDecorator):
    def __init__(self, cart_pricing : CartPricing, item_id : str, discount : double):
        self.cart_pricing = cart_pricing
        self.item_id = item_id
        self.discount = discount
    def calculate_total(self):
        for item in self.cart_pricing.get_items():
          if item.id == self.item_id:
            return (self.cart_pricing.calculate_total() - self.discount)
        # the discounted item was not found
        return self.cart_pricing.calculate_total()


# FreeShipping inherits CartDecorator
class FreeShipping (CartDecorator):
    def __init__(self, cart_pricing : CartPricing):
      self.cart_pricing = cart_pricing
    def get_shipping() -> float:
      return 0.0
    # def calculate_total(self):
    #     return cart_pricing.calculate_total() # total stays the same



def main():
    item1 = Item("123", "shoes", 100)
    item2 = Item("456", "shirt", 50)
    items = [item1, item2]
    cart = BaseCart(items, 10)
    print(cart.calculate_total())
    print(cart.calculate_final_price())
    cart = CartDiscount(cart, 0.20)
    print(cart.calculate_total())
    print(cart.calculate_final_price())
    cart = ItemDiscount(cart, "123", 5)
    print(cart.calculate_total())
    print(cart.calculate_final_price())
    cart = FreeShipping(cart)
    print(cart.calculate_total())
    print(cart.calculate_final_price())

if __name__ == "__main__":
    main()
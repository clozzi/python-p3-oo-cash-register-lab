#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, discount):
    if isinstance(discount, (int, float)):
      self._discount = discount
    else:
      print("not a number")

  def add_item(self, title, price, quantity=1):
    self.items.extend([(title, price)] * quantity)
    self.total += (price * quantity)

  def apply_discount(self):
    if self._discount > 0:
      discount_amt = self.total * (self._discount / 100)
      self.total -= discount_amt
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")

  def get_items(self):
      return list(self.items)
  
  def void_last_transaction(self):
    if self.items:
      last_price = self.items[-1][1]
      self.items.pop()
      self.total -= last_price
    else:
      print("No items to remove.")

  
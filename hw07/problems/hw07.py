class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    """

    def __init__(self):
        self.value = 0

    def next(self): #its a recursive calling be carefull 
        "*** YOUR CODE HERE ***"
        #next被连续调用的次数作为迭代器 实际是返回self的次数? 返回新的Fib/返回本身对象 
        #返回新对象考虑如何传值,返回对象本身要考虑如何迭代
        newfib = Fib()
        if self.value == 0:#
            newfib.value = 1
            newfib.prev = 0
        elif self.value ==1 and self.prev == 0:
            newfib.value = 1
            newfib.prev = self.value
        else:
            newfib.prev = self.value
            newfib.value = self.value + self.prev
        return newfib
    def __repr__(self):
        return str(self.value)
'''
#this function helps to solve the problem            
def next(fib):
    newfib = Fib()
    if fib.value == 0:#
       newfib.value = 1
       newfib.prev = 0
    elif fib.value ==1 and fib.prev == 0:
        newfib.value = 1
        newfib.prev = fib.value
    else:
        newfib.prev = fib.value
        newfib.value = fib.value + fib.prev
    return newfib
'''             

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,goods,price):
        self.goods = goods
        self.stock = 0
        self.price = price 
        self.balance = 0
    def vend(self):
        if self.stock <= 0:
            return 'Machine is out of stock.'
        elif self.balance < self.price:
            return 'You must deposit $' + str(self.price - self.balance) +' more.'
        elif self.balance == self.price:
            self.stock -=1
            self.balance = 0
            return 'Here is your ' + self.goods +   '.'
        else:
            change =  self.balance - self.price
            self.stock -=1
            self.balance = 0
            return 'Here is your ' + self.goods +  ' and $' + str(change) + ' change.'            
    def restock(self,n):
        self.stock +=n
        return   'Current ' + self.goods +' stock: ' + str(self.stock)
    def deposit(self,money):
        self.balance += money
        if self.stock <= 0:
            return 'Machine is out of stock. Here is your $' + str(self.balance) + '.'
        else:
            return 'Current balance: $' + str(self.balance) 
import re
rule=re.compile(r'[^a-zA-z]')
class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> double_fussy = MissManners(m) # Composed MissManners objects
    >>> double_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> double_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> double_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> double_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    def __init__(self, obj):
        self.obj = obj

    def ask(self, message, *args):
        magic_word = 'please '
        if not message.startswith(magic_word):
            return 'You must learn to say please first.'
        "*** YOUR CODE HERE ***"
        order = message[7:]
        if hasattr(self.obj, order):
            return getattr(self.obj, order)(*args)
        else:
            return 'Thanks for asking, but I know not how to {0}.'.format(order)
        


            

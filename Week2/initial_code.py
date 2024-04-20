"""
Module for working in a coffee shop
(creating an order, checking recipes, adding flavours, etc.)
"""
RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }
class Track:
    """
    Class track for order tracking, which contains attributes
    - data and order, as well as various methods
    """
    __beans = 5000
    __milk = 20000
    safety = True
    def __init__(self, date: str) -> None:
        """
        Initalization of class objects of Track
        """
        self.date = date
        self.orders = []

    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60
    }

    def place_order(self, order):
        """
        A method for checking whether the order can be accepted,
         as well as for accepting the order itself
        """
        if isinstance(order, str):
            return "We can't create anything that is not a Coffee instance."
        if not self.safety:
            return 'Unfortunately, now it is not safe to make coffee.'
        if order.name not in self.MENU:
            return "Unfortunately, we don't have such kind of coffee in the menu."
        if self.milk - order.milk < 0:
            return "Unfortunately, we don't have enough ingredients."

        self.orders.append(order)
        order.is_paid = True
        order.price = Track.MENU[order.name] * order.count


        return 'Done!'

    def total_revenue(self):
        """
        Method for count total revenue
        """
        count = 0
        for i in self.orders:
            count += Track.MENU[i.name] * i.count

        return count
    def total_milk(self):
        """
        Method for count total milk
        """
        m_count = 0
        for i in self.orders:
            m_count += i.milk
        return m_count
    def total_beans(self):
        """
        Method for count total beans
        """
        b_count = 0
        for i in self.orders:
            b_count = b_count + (RECIPE[i.name]['espresso'] // 30) * 6 * i.count
        return b_count
    @property
    def beans(self):
        """
        Method to change amount of beans
        """
        return self.__beans - self.total_beans()

    @property
    def milk(self):
        """
        Method to change amount of milk
        """
        if self.__milk < 0:
            return 0
        return self.__milk - self.total_milk()

    def milk_spoil(self, value):
        """
        Method milk spoil
        """
        self.__milk -= value
    @classmethod
    def set_limit_milk(cls, value):
        """
        Method to make own limit of milk
        """
        cls.__milk = value
    @classmethod
    def change_air_state(cls):
        """
        Method to change air state
        """
        if cls.safety:
            cls.safety = False
        else:
            cls.safety = True


class Coffee:
    """
    Class coffee for work with all information and oportunities about coffee,
    which contains attributes - name, count
    """
    __recipe = {}
    def __init__(self, name: str, count=1):
        """
        Initalization of class objects of Coffee
        """
        self.name = name
        self.count = count
        if self.name in self.__recipe:
            self.is_paid = False

    @classmethod
    def set_recipe(cls, recipe):
        """
        Class method to set recipe
        """
        cls.__recipe = recipe

    def __str__(self) -> str:
        """
        Realization string representation of an object
        """
        if not self.name in RECIPE:
            return "Order cannot be created. We don't have recipe for it."
        if not self.__recipe:
            return "Order cannot be created. Recipe has not been set."
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        if self.__recipe:
            return f'Order "{self.count} {self.name}" is created.'

    @property
    def espresso(self):
        """
        Method to count amount of espresso
        """
        return self.count * RECIPE[self.name]['espresso']

    @property
    def milk(self):
        """
        Method to count amount of milk
        """
        m_count = 0
        if 'steamed_milk' in RECIPE[self.name]:
            m_count = m_count + RECIPE[self.name]['steamed_milk'] * self.count
        if 'foamed_milk' in RECIPE[self.name]:
            m_count = m_count + RECIPE[self.name]['foamed_milk'] * self.count
        return m_count

    def __repr__(self):
        """
        Realization string representation of an object
        """
        return f'{self.count} {self.name}'

    def __eq__(self, value):
        """
        Method to compare two classes
        """
        return self.name == value.name and self.count == value.count

class FlavorMixin:
    """
    Class FlavorMixin for adding different flavors,
    which contains attributes - sugar, cinammon, syrup, flavor
    """
    def add_flavor(self, sugar: int, cinammon: bool, syrup: str):
        """
        Method for initalization of class objects of FlavorMixin
        """
        if self.is_paid:
            self.sugar = sugar * self.count
            self.cinammon = cinammon
            self.syrup = syrup
            self.flavor = True
            return 'Done!'
        return 'Please, pay for it.'

class CustomCoffee(Coffee, FlavorMixin):
    """
    Class CustomCoffee for creating custom coffee,
    which contains attributes from inheritance classes and flavor
    """

    def __init__(self, name: str, count=1):
        """
        Initalization of class objects of CustomCoffee
        """
        super().__init__(name, count)
        self.flavor = False

    def __str__(self):
        """
        Realization string representation of an object
        """
        if self.flavor:
            text = f'Your best {self.name} is ready! It has:'
            if self.sugar:
                text += f' {self.sugar} stickers of sugar,'
            if self.cinammon:
                text += ' cinammon,'
            if self.syrup:
                text += f' {self.syrup} syrup,'
            text = text.rstrip(', ')
            return text + '.'

        if not self.name in RECIPE:
            return "Order cannot be created. We don't have recipe for it."
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self.count} custom {self.name}" is created.'
    def __repr__(self):
        """
        Realization string representation of an object
        """
        return f'{self.count} custom {self.name}'

    def __eq__(self, value):
        """
        Method to compare two classes
        """
        if isinstance(value, CustomCoffee):
            return super().__eq__(value) and self.sugar == value.sugar\
                  and self.syrup == value.syrup and self.cinammon == value.cinammon
        return super().__eq__(value)
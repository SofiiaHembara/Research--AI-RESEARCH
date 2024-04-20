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
        "espresso": 40,
        "latte": 70,
        "flat white": 70,
        "dopio": 50,
        "cappuccino": 60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60
    }

    def place_order(self, order):
        """
        A method for checking whether the order can be accepted,
         as well as for accepting the order itself
        """
        if not isinstance(order, Coffee):
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
            b_count += RECIPE[i.name]['espresso'] // 30 * 6 * i.count
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
    
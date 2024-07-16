class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._quantity = 0

    def __str__(self):
        print("Nu caut emoji de cookie", "#" * self._quantity)

    def deposit(self, n):
        if n + self._quantity > self._capacity:
            raise ValueError

        self._quantity += n

    def withdraw(self, n):
        if self._quantity - n < 0:
            raise ValueError

        self._quantity -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._quantity

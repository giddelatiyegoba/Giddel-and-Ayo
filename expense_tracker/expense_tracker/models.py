class Entry:
    def __init__(self, name, amount, category=None, date_time=None):
        self.name = name
        self.amount = amount
        self.category = category
        self.date_time = date_time

    def to_row(self, type="expense"):
        return [self.name, self.amount, self.category or "", self.date_time, type]

class Expense(Entry):
    pass

class Income(Entry):
    def __init__(self, name, amount, date_time=None):
        super().__init__(name, amount, category="income", date_time=date_time)

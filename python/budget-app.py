"""
一个记录每种类别每个条目支出的 记账App

create_spend_chart 函数比较有特点，它将各个类别的支出占比使用条形图的方式展示出来
"""

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0  # total money

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
        self.total += amount # add money

    def withdraw(self, amount, description = ''):
        self.ledger.append({'amount': -1 * amount, 'description': description})
        if self.check_funds(amount):
            self.total -= amount # minus money
            return True
        return False

    def get_balance(self):
        return self.total

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other.name}')
            other.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.total >= amount

    def __str__(self):
        res = f'{self.name.center(30, "*")}\n'
        for item in self.ledger:
            amount = item['amount']
            amount = f'{amount:.2f}'
            description = item['description']
            res += f'{description[:23].ljust(23)}{amount[-7:].rjust(7)}\n'

        res += f'Total: {self.get_balance():.2f}'
        return res


def create_spend_chart(categories):
    res = 'Percentage spent by category\n'
    all_withdraws = [e['amount'] for category in categories for e in category.ledger if e['amount'] < 0]
    total_spend = sum(all_withdraws)
    # store percentage of each category
    percentage_list = []
    for category in categories:
        withdraws = [e['amount'] for e in category.ledger if e['amount'] < 0]
        spend = sum(withdraws)
        # 计算消费比率
        rate = 10 * spend // total_spend * 10
        print(f'{category.name} percentage: {rate}')
        # percentage list of categories
        percentage_list.append({'name': category.name, 'percentage': rate})

    # draw chart according to percentage list
    # 1. draw rate segment and flag 'o'
    for i in range(100, -1, -10):
        # align to the right
        row = (str(i) + "|").rjust(4, ' ')
        for index, item in enumerate(percentage_list):
            percentage = item['percentage']
            if percentage >= i:
                row += ' o '
            else:
                row += ' ' * 3
        res += row + ' \n'

    # 2. draw spliter linie
    res += ' ' * 4 + '-' * len(percentage_list) * 3 + '-\n'
    # get names
    names = [item['name'] for item in percentage_list]
    # get the max length of name
    max_len = max([len(name) for name in names])
    for i in range(max_len):
        res += ' ' * 4;
        for name in names:
            if i < len(name):
                res += f' {name[i]} '
            else:
                res += ' ' * 3
        res += ' \n'
    res = res[:-1]
    return res

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(12.8, 'cake')
print(food)

categories = [food, clothing]
print(create_spend_chart(categories))

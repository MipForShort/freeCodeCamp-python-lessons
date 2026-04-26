class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -abs(amount), 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):
        output = ''
        output += self.name.center(30, '*') + '\n'
        for item in self.ledger:
            output += f'{item["description"][:23]:<23}{item["amount"]:>7.2f}\n'
        output += f'Total: {self.get_balance():.2f}'
        return output

def create_spend_chart(categories):
    output = 'Percentage spent by category\n'
    spent = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += item['amount']
        spent.append(-total)
    total_spent = sum(spent)
    percentages = []
    for amount in spent:
        percent = (amount / total_spent) * 100
        percent = int(percent // 10) * 10
        percentages.append(percent)

    for i in range(100, -1, -10):
        line = f"{i:>3}| "
        for percent in percentages:
            if percent >= i:
                line += "o  "
            else:
                line += "   "
        output += line + "\n"
    
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(c.name) for c in categories)

    for i in range(max_len):
        line = "     "

        for c in categories:
            if i < len(c.name):
                line += c.name[i] + "  "
            else:
                line += "   "

        output += line + "\n"
    return output.rstrip("\n")

if __name__ == '__main__':
    food = Category('Food')
    food.deposit(1000, 'initial deposit')
    food.withdraw(10.15, 'groceries')
    food.withdraw(15.89, 'restaurant and more food for dessert')
    clothing = Category('Clothing')
    food.transfer(50, clothing)
    print(food)
    print(clothing)
    print(create_spend_chart([food, clothing]))
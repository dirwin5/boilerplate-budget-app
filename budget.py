class Category:
      
    def __init__(self, cat_name):
        self.cat_name = cat_name
        self.ledger = []
        self.balance = 0
        self.cat_name_len = len(cat_name)
        self.spent = 0
        
    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
                
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": (amount * -1), "description": description})
            self.balance -= amount
            self.spent += amount
            return True
        else:
            return False
            
    def get_balance(self):
        return self.balance
        
    def transfer(self, amount, dest_cat_name):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": (amount * -1), "description": f"Transfer to {dest_cat_name.cat_name}"})
            self.balance -= amount
            dest_cat_name.ledger.append({"amount": amount, "description": f"Transfer from {self.cat_name}"})
            dest_cat_name.balance += amount
            return True
        else:
            return False
            
    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True
        
    def __str__(self):
        title_line = []
        ast_no = 30 - self.cat_name_len
        for ast in range(int(ast_no/2)):
            title_line.append('*')
        title_line.append(self.cat_name)
        for ast in range(int(ast_no/2)):
            title_line.append('*')
        title_line.append('\n')
        title_line = ''.join(title_line)
        
        ledger_lines = []
        for line in self.ledger:
            desc = line["description"][:23]
            desc_ws = 23 - len(desc)
            ledger_lines.append(desc)
            for ws in range(desc_ws):
                ledger_lines.append(' ')
                
            am = line["amount"]
            am = '{0:.2f}'.format(am)
            am_ws = 7 - len(am)
            for ws in range(am_ws):
                ledger_lines.append(' ')
            ledger_lines.append(am)
            ledger_lines.append('\n')
        ledger_lines = ''.join(ledger_lines)
        
        tot_line = f"Total: {round(self.balance, 2)}"
         
        prnt_output = f"{title_line}{ledger_lines}{tot_line}"
            
        return prnt_output
            


def create_spend_chart(categories):
    cat_no = len(categories)
    spent = []
    total_spent = 0
    for cat in categories:
        spent.append(cat.spent)
        total_spent += cat.spent
        
    spent_pcnt = []
    for value in spent:
        pcnt = value / total_spent * 100
        pcnt = (pcnt // 10) * 10
        spent_pcnt.append(pcnt)
        

    title_line = 'Percentage spent by category\n'
    
    bar_value = 100
    bar_chart = []
    
    for line in range(11):
        bar_value_ws = 3 - len(str(bar_value))
        for ws in range(bar_value_ws):
            bar_chart.append(' ')
        bar_chart.append(str(bar_value))
        bar_chart.append('| ')
        for pcnt in spent_pcnt:
            if pcnt >= bar_value:
                bar_chart.append('o  ')
            else:
                bar_chart.append('   ')
        bar_chart.append('\n')
        bar_value -= 10
    
    bar_chart.append ('    -')
    for pcnt in spent_pcnt:
        bar_chart.append('---')
    bar_chart.append('\n')
    
    max_name_len = 0
    for category in categories:
        if category.cat_name_len > max_name_len:
            max_name_len = category.cat_name_len
        
    
    i = 0
    for line in range(max_name_len):
        bar_chart.append('     ')
        for category in categories:
            try:
                bar_chart.append(category.cat_name[i])
            except IndexError:
                bar_chart.append(' ')
            bar_chart.append('  ')
        bar_chart.append('\n')
        i += 1
    
    bar_chart.pop()
    
    bar_chart = ''.join(bar_chart)
    
    outpt = f"{title_line}{bar_chart}"
    
    return outpt
    
            
        
    
    
#Homework 1
#William O'Brochta

#hw1_testing file contains full tests for the program

class Portfolio():
    def __init__(self,Cash=0):
        self.Cash=float(Cash)
        #Create dictionary for list of stocks and price and a list for the funds since their price is 1.
        #Create dictionaries for stocks and funds purchased.
        #Create history for all the transactions.
        self.Stock_List={}
        self.Stock_Bought={}
        self.MutualFund_List=[]
        self.MutualFund_Bought={}
        self.history=[]
        self.history.append("This is your account in the Tajik National Bank. I started with %s somoni in cash." %(self.Cash))
    
    #Initialize the print command.
    def __str__(self):
        return "I have %.2f somoni in cash.\nI have the following names and amounts of stock: %s.\nI have the following names and amounts of mutual funds: %s." %(self.Cash, self.Stock_Bought, self.MutualFund_Bought)
    
    def addCash(self, add):
        self.Cash=float(self.Cash)+float(add)
        self.history.append("I added %s somoni and have %s somoni total." %(add,self.Cash))
        return "I added %s somoni and have %s somoni total." %(add,self.Cash)
 
    def withdrawCash(self,withdraw):
        self.Cash=float(self.Cash)-float(withdraw)
        self.history.append("I withdrew %s somoni and have %s somoni total." %(withdraw,self.Cash))
        return "I withdrew %s somoni and have %s somoni total." %(withdraw,self.Cash)

    def Stock(self,price,stock_symbol):
        #Add stocks to the dictionary.
        self.Stock_List[stock_symbol]=price
        self.history.append("I added %s stock at a price of %s somoni to my list." %(stock_symbol,price))
        return "I added %s stock at a price of %s somoni to my list." %(stock_symbol,price)
    
    def buyStock(self,amount,stock_symbol):
        #Check to see if there's enough money to buy the stock.
        if self.Cash < float(amount*float(self.Stock_List[stock_symbol])):
            self.history.append("Insufficient funds. :( I tried to buy stocks that I cannot!")
            return "Insufficient funds. :("
        else:
            self.Cash=self.Cash-float(amount*float(self.Stock_List[stock_symbol]))
            if stock_symbol in self.Stock_Bought:
                self.Stock_Bought[stock_symbol].add(amount)
            else: self.Stock_Bought[stock_symbol]=amount
        self.history.append("I bought %s shares of %s stock. I have %s somoni available in cash." %(amount, stock_symbol, self.Cash))
        return "I bought %s shares of %s stock. I have %s somoni available in cash." %(amount, stock_symbol, self.Cash)        
        
    def MutualFund(self,name):
        self.MutualFund_List.append(name)
        self.history.append("I added %s mutual fund." %(name))
        return "I added %s mutual fund." %(name)
        
    def buyMutualFund(self,amount,mf_symbol):
        if self.Cash < amount:
            self.history.append("Insufficient funds. :( I tried to buy funds that I cannot!")
            return "Insufficient funds. :("
        else:
            self.Cash=self.Cash-amount
            if mf_symbol in self.MutualFund_Bought:
                self.MutualFund_Bought[mf_symbol].add(amount)
            else: self.MutualFund_Bought[mf_symbol]=amount
        self.history.append("I bought %s shares of %s fund. I have %s somoni available in cash." %(amount, mf_symbol, self.Cash))
        return "I bought %s shares of %s fund. I have %s somoni available in cash." %(amount, mf_symbol, self.Cash)        

    def sellMutualFund(self,amount,mf_symbol):
        import random
        #Pull random integer from 0.9 to 1.2
        random1=random.uniform(0.9,1.2)
        #Check to see if the fund exists in the list.
        if mf_symbol not in self.MutualFund_Bought:
            self.history.append("I tried to sell a mututal fund I do not own!")
            return "I tried to sell a mututal fund I do not own!"
        else:
        #Check to see if user is trying to sell too many funds.
            if self.MutualFund_Bought[mf_symbol] < amount:
                self.history.append("Trying to sell too many funds!")
                return "Trying to sell too many funds!"
            else:
                self.Cash=self.Cash+float(amount*random1)
                self.MutualFund_Bought[mf_symbol]=float(self.MutualFund_Bought[mf_symbol])-amount
            self.history.append("I sold %s shares of %s fund. I have %.2f somoni available in cash." %(amount, mf_symbol, self.Cash))
            return "I sold %s shares of %s fund. I have %.2f somoni available in cash." %(amount, mf_symbol, self.Cash)

    def sellStock(self,amount,stock_symbol):
        import random
        random1=random.uniform(0.5,1.5)
        if stock_symbol not in self.Stock_Bought:
            self.history.append("I tried to sell stock I do not own!")
            return "I tried to sell stock I do not own!"
        else:
            if self.Stock_Bought[stock_symbol] < amount:
                self.history.append("Trying to sell too many stocks!")
                return "Trying to sell too many stocks!"
            else:
                self.Cash=self.Cash+float(amount*random1*float(self.Stock_List[stock_symbol]))
                self.Stock_Bought[stock_symbol]=float(self.Stock_Bought[stock_symbol])-amount
            self.history.append("I sold %s shares of %s stock. I have %.2f somoni available in cash." %(amount, stock_symbol, self.Cash))
            return "I sold %s shares of %s stock. I have %.2f somoni available in cash." %(amount, stock_symbol, self.Cash)

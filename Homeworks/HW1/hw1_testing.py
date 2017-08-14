#Homework 1: Testing File
#William O'Brochta

#This file tests all the functions of the class portfolio.

portfolio=Portfolio(5)
portfolio.addCash(1000)
portfolio.withdrawCash(2)
portfolio.Stock(2,"IBM")
portfolio.Stock(2,"ATT")
portfolio.buyStock(30,"IBM")
portfolio.sellStock(2,"ATT")
portfolio.buyStock(2,"ATT")
portfolio.MutualFund("Schwab")
portfolio.MutualFund("Vangard")
portfolio.MutualFund("Fidelity")
portfolio.MutualFund("UBS")
portfolio.buyMutualFund(40.5,"Vangard")
portfolio.buyMutualFund(5000,"Schwab")
portfolio.buyMutualFund(50,"Schwab")
portfolio.buyMutualFund(10,"Fidelity")
portfolio.buyMutualFund(1.5,"UBS")
portfolio.sellMutualFund(3,"Schwab")
portfolio.sellMutualFund(2,"Vangard")
portfolio.sellStock(10,"IBM")
portfolio.history
print portfolio

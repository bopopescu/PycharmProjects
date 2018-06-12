# polymorphism : method with  return values , not by  only method name like abstract method

class Bank:

    def setRateofInterest(self):
        self.rate = 16.50


    def getRateofInterest(self):
        return self.rate

class HDFC(Bank):


    def setRateofInterest(self):
        self.rate = 14.00


    def getRateofInterest(self):
        return self.rate


# bank = Bank() #erroroccurs child class not declared
# bank.setRateofInterest()
# print(bank.getRateofInterest())

hdfc = HDFC()
hdfc.setRateofInterest()
print(hdfc.getRateofInterest())
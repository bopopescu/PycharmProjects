# # data abstraction # purely depends on method oveeriding
#
# class Bank:
#
#     def setRateofInterest(self):
#         #self.rate = 16.50
#         raise NotImplementedError("only subclasses can ")
#
#     def getRateofInterest(self):
#         #return self.rate
#         raise NotImplementedError("only subclasses can ")
#
# bank = Bank()
# bank.setRateofInterest()
# print(bank.getRateofInterest())

# data abstraction # purely depends on method oveeriding

class Bank:

    def setRateofInterest(self):
        raise NotImplementedError("only subclasses can implement")

    def getRateofInterest(self):
        raise NotImplementedError("only subclasses can implement ")

class HDFC(Bank):


    def setRateofInterest(self):
        self.rate = 16.50


    def getRateofInterest(self):
        return self.rate


# bank = Bank() #erroroccurs child class not declared
# bank.setRateofInterest()
# print(bank.getRateofInterest())

hdfc = HDFC()
hdfc.setRateofInterest()
print(hdfc.getRateofInterest())
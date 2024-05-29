class MovieTicket():
    basePrice=10
    def __init__(self,fee):
        self.basePrice=20
        self.price=self.basePrice+fee
x=MovieTicket(5)
print(x.price)
print(MovieTicket.basePrice)

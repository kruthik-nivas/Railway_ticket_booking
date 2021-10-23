class Passenger:

    def __init__(self,customerID,name,age,gender,preference):
        self.customerId = customerID
        self.name=name
        self.age=i=age
        self.gender=gender
        self.preference=preference
        self.status=''
        self.seat = None

    def printTickets(self):
        print(f"Customer ID -> {self.customerId}")
        print(f"Name: {self.name}")
        print(f"Age -> {self.age}")
        print(f"Tciket Stauts -> {self.status}")
        if self.seat != None:
            print(f"Seat -> {self.seat}")
        else:
            print('Seat Not allocated')
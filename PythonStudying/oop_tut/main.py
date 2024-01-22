import csv


class Item: 
    all = []
    #Atributes
    pay_rate = 0.8 #The pay rate after 20% discounter

    #constuctor
    def __init__(self, name: str, price: float, quantity=0 ):
       #Run validations to the recieve arguments
        assert price >= 0, f"price {price} is not greater or equal than zero"
        assert quantity >= 0, f"price {price} is not greater or equal than zero"
       
       #Assign to self object
        self.price = price
        self.name = name
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f'The device type is {self.name}, {self.price}'


    def calculate_total_price(self):
        return self.price * self.quantity
    

    def appy_discoun(self):
        self.price = self.price * self.pay_rate

    
    @classmethod
    def instanciate_from_csv(cls):
        with open('D:/PythonStudying/opp_tut/data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)


Item.instanciate_from_csv()
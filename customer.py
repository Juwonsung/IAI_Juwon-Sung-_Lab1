from book_info import book_lists

class Customer():
    def __init__(self):
        pass

    def regis_customer(self , name , age):
        self.name = name
        self.age = age
        print(f"customer name is {self.name} , {self.age}")
        
        return self.name, self.age
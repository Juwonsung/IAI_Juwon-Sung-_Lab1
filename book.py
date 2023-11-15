from book_info import book_lists
from customer import Customer


class Book(Customer):
    # def regis_customer(self , name , age):
    #     self.name = name
    #     self.age = age
    #     print(f"customer name is {self.name} , {self.age}")
    #     return self.name, self.age
    #
    def book_manag(self):
        wanted_book = []
        while True:
            answer = input("Do you wanna borrow or return or no? (borrow/return/no) :")
            # split the cases
            if answer == "no":
                break

            elif answer == "borrow":
                bo_want_book = input("which books do you wanna borrow?:")
                wanted_book.append(bo_want_book)
                for book in book_lists:
                    if bo_want_book == book['title']:
                        book["status"] = "borrowed"

            elif answer == "return":
                re_want_book = input("which books do you wanna return?:")
                for book in book_lists:
                    if re_want_book == book["ti`your text`tle"]:
                        book["status"] = "available"

        return wanted_book


book_m = Book()  # define class
print("\n")



"""
Solve this task with recursive programming.
In this exercise you have to find how much cookies can be consumed 
with the given amount of money.

money: Starting money, to spend for cookies
price: Price of the cookie
wrap: Number of wrappers to be returned for getting one extra cookie.
It may be assumed that all given values are positive integers and greater than 1.
"""

#solution with classs
class Cookies:
    def __init__(self) -> None:
        self.all_cookies:int = 0

    def calculate_cookies(self,money:int,price:int,wrap:int):
        if money >= price:
            cookies = money // price
            self.all_cookies += cookies
            if cookies >= wrap:
                return self.calculate_cookies(cookies,wrap,wrap)


#solution with only functions
def get_those_cookies(money:int,price:int,wrap:int):

    def calculate_cookies(money:int,price:int,wrap:int,all_cookies:int=0):
        if money >= price:
            cookies = money // price
            all_cookies += cookies
            if cookies >= wrap:
                return calculate_cookies(cookies,wrap,wrap,all_cookies)
        return all_cookies

    return calculate_cookies(money,price,wrap)


#c = Cookies()
#c.calculate_cookies(100,2,50)
#print(c.all_cookies)

print(get_those_cookies(100,2,3))





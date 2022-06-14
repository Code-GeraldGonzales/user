from operator import truediv


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

#  display_info(self) - Have this method print all of the users' details on separate lines.

    def display_info(self):
        print(self.first_name, self.last_name)
        print(f"Email {self.email}")
        print(f"Is {self.age} years old")
        print(f"Is {self.is_rewards_member}")
        print(f"Has {self.gold_card_points} points")
        return self

#  enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

    def enroll(self):
        if self.is_rewards_member:
            print('True is a rewards member')
        else: 
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self



    def spend_points(self,amount):
        if amount > self.gold_card_points:
            print("You Don't Have Eough Points")
        else: 
            self.gold_card_points -= amount
        return self



user_1 = User("Jerry", "Gonzales", "dude@dude.com", 53)
User_2 = User("Armando", "Gonzales", "son@son.com", 24)
User_3 = User("Caitlyn", "Gonzales", "daughter@daughter.com", 22)
user_1.display_info().enroll().spend_points(50).display_info()
User_2.display_info().enroll().spend_points(80)
User_3.display_info().spend_points(40)



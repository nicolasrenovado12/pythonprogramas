class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")
        
user1 = User("Peter", "peter@gmail.com", "peter123")
user2 = User("Batman", "bat@outlok.com", "abc")

user1.say_hi_to_user(user2)
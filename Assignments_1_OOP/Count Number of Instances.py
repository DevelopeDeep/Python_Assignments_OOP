class User:
    count = 0

    def __init__(self):
        self.username = input("Enter Username : ")
        User.count += 1

    def usercount(self):
        print("User : ", self.username, User.count)

def main():
    user1 = User()
    user1.usercount()

    user2 = User()
    user2.usercount()

    user3 = User()
    user3.usercount()

if __name__=="__main__":
    main()
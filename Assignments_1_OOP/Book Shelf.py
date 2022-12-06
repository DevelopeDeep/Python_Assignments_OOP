class Book:

    def __init__(self):
        self.title = input("Enter Title : ")
        self.author = input("Enter Author : ")

    def get_title(self):
        print("Title : {} ".format(self.title))

    def get_author(self):
        print("Author : {} ".format(self.author))

def main():
    obj = Book()
    obj.get_title()
    obj.get_author()

if __name__=="__main__":
    main()
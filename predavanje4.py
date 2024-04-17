#napraviti jedno klase user ,napravote konstruktor

class User:
    def __init__(self):
        print("User init")

    def who_am_I(self):
        print("I'm user")

    def login(self):
        print("User login")

class Admin(User):
    def __init__(self):
        User.__init__(self)
        print("Admin")
    def delete_user(self):
        print("I can delete users.")

user1=User()
admin1=Admin()
admin1.who_am_I()
#user1.delete_user()
#napravite klase pravougaonik ,napravite konstruktor koji ce predstavite sirinu i duzinu prav.

class Rectangle:
    def __init_(self,width,height):
        self.__width=width
        self.__height=height
    def area(self):
        return self.__width*self.__height
    def perimetar(self):
        return 2*self.__width*2*self.__height
    def set_eidth(self,new_width):
        if new_width= 0:
            self.__width=new_width
        else:
            print("unijeti ste vrijednost koja je manja od nule")
    def get_width(self):
        return self
class Square(Rectangle):
    def __init__(self,width,color):
        super().__init__(width,width)
        self.__color= color
    def fill(self):
        print(f"fill with{self.__color} color")

rectangle1 = Rectangle(2,3)
print(rectangle1.area())
print(rectangle1.perimetar())
square1=Square(2, 'red')
print(square1.area())
print(square1.perimetar())
square1.fill() 
rectangle1



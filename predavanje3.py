class Post:
    class_var_author="Admin"
    def __init__(self,name,description,author,id):
        self.name=name
        self.description= description
        self.author= author
        self.id=id

class Circle:
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return self.radius**2*Circle.pi
    
    def set_radius(self,new_radius):
        self.radius= new_radius

    def get_radius(self):
        return self.radius

c1=Circle(10)
print(c1.area())
c1.radius=20
print(c1.area())






"""
post_first = Post("First Post", "This is the first post","Admin", 1)
post_second = Post("Second post","AI in programming","Admin",2)
print(post_first.name)
print(post_second.author)#instance me p te vogel
print(Post.class_var_author)#naziv klase me P te madh
print(type(post_first))
"""

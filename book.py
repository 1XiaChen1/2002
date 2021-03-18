class Book:
    """
書名   書號   類別   定價   ISBN"""
    def __init__(self,Class,department,number,name,nickname):
        self.name=name
        self.number=number
        self.department=department
        self.nickname=nickname
        self.Class=Class
    def showinfo(self):
        print(self.Class,"\t",self.department,"\t",self.number,"\t",self.name,"\t",self.nickname)
x=Book("基礎程式設計","666666","資訊與工程","168","000-000-001")
y=Book("進階程式設計","888888","資訊與工程","168","000-001-010")
z=Book("程式設計與程式應用","222222","資訊與工程","857","001-010-100")
print(Book.__doc__)
x.showinfo()
y.showinfo()
z.showinfo()

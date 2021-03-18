class Student:
    """
班級   科系   學號   姓名   小名"""
    def __init__(self,Class,department,number,name,nickname):
        self.name=name
        self.number=number
        self.department=department
        self.nickname=nickname
        self.Class=Class
    def showinfo(self):
        print(self.Class,"\t",self.department,"\t",self.number,"\t",self.name,"\t",self.nickname)
x=Student("B","資工","109000333","王老吉","老王")
y=Student("C","資工","109111555","夏死伱","老夏")
z=Student("A","資工","109222999","郭紙錢","小郭")
print(Student.__doc__)
x.showinfo()
y.showinfo()
z.showinfo()

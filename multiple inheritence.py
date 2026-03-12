class GrandFather:
    def G1(self):
        print("this is grandparent class")
class Father:
    def F1(self):
        print("this is father class")
        
class child(Father,GrandFather):
    def C1(self):
        print("this is child class")

c=child()
c.C1()
c.F1()
c.G1()

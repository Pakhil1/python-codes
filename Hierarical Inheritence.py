class Father():
    def F1(self):
        print("This is Father class")
class Child1(Father):
    def C1(self):
        print("This is Child1 class")
        
class Child2(Father):
    def C2(self):
        print("This is Child2 class")

c2=Child2()
c2.C2()
c2.F1()

c2=Child1()
c2.C1()
c2.F1()

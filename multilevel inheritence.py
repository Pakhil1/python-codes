class Father():
    def p1(self):
        print("this is Father class")
        
class Mother(Father):
    def m1(self):
        print("this is Mother class")
        
class Child(Mother):
    def C1(self):
        print("This is Child class")
  
c=Child()
c.C1()
c.m1()
c.p1()
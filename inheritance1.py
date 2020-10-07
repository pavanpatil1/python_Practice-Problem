class A(object):

    def __init__(self, a):
        self.a = a
    
    def __str__(self):
        return "a="+str(self.a)

    def display(self):
        print self.a

class B(A):

    def __init__(self, a, b):
        super(B, self).__init__(a)
        self.b = b

    def sum(self):
        return self.a + self.b
    
    def __str__(self):
        return A.__str__(self) + " b=" + str(self.b)

    # def display(self):
    #     print self.a


b = B(10,20)
b.display()


# data = []

# while(True):
#     print "1. Add record"
#     print "2. Search record"
#     print "3. Exit"

#     ch = input("Enter choice:")

#     if ch == 1:
#         a = input("Enter the value of a:")
#         b = input("Enter the value of b:")
#         data.append(B(a,b))
#     elif ch == 2:
#         a = input("Enter the roll to be searched:")
#         for d in data:
#             # print d.a
#             if d.a == a:
#                 print d
#                 break
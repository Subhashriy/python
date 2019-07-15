class A:
    def m1(self):
        return 'm1 method of A'
    def m2(self):
        return 'm2 method'

class B():#inheritance
    def m1(self):
        return 'm1 method of B'
    def m4(self):
        return 'm4 method'


class C(A):
    def m5(self):
        return 'inheritance'


class D(B,C):
    def m6(self):
        return 'hierarchical'

a=A()  #m1,m2
print(a.m1())
print(a.m2())

b=B()  #m3,m4
print(b.m1())
#print(b.m2())
'''print(b.m1())
print(b.m2())'''


print()
c=C()
print(c.m5())
print(c.m1())
print(c.m2())

print()

d=D()
'''print(d.m6())
print(d.m5())
print(d.m1())
print(d.m1())
'''


print(issubclass(D,A))
print(isinstance(d,D))
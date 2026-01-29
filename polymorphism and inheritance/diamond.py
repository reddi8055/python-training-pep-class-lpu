class A:
    print("A")
class B(A):
    print("B")
class C(A):
    print("C")
class D(B, C):
    print("D")
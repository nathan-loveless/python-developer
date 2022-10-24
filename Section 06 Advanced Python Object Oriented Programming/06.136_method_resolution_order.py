# Method Resolution Order (MRO)
#     A
#  /     \
# /       \
# B        C
# \       /
#  \     /
#     D

# MRO - D -> B -> C -> A
# mro() gives you the order Python will check for methods/attributes
# print(D.mro())

class X: pass


class Y: pass


class Z: pass


class A(X, Y): pass


class B(Y, Z): pass


class M(B, A, Z): pass


# MRO uses Depth first search as the algorithm for which order to check inherited classes
print(M.mro())

# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>,
# <class '__main__.Z'>, <class 'object'>]

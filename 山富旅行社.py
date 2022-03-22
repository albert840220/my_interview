# 1.
class Dog(object):

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

# 2.*args **kwargs 請用100字解釋
# 3.python environment 是什麼？如何管理？請用50字解釋
# 4. add=lambda x,y: x+y,請寫成def
# 5.
print(list ( map ( lambda x: x ** 2 , [ 1 , 2 , 3 , 4 , 5 ] ) ))   # 使用lambda 匿名函數
# Ans: [ 1 , 4 , 9 , 16 , 25 ]

def f1(): 
  print("oi!")

f1()
"""
"oi"
oi
"oi!"
oi!
Nada
"""

def f2():
  print(2 + 4 * 65 / 2)

f2()
"""
132
131
195
130
Nada
"""

def f3(): 
  print(40 % 10) # resto da divisão inteira
  return 0
  print(40/10)

f3()
"""
4, 0 e 4
40 e 4
0, 0 e 4
0 e 0
0
0 e 4
4
Nada
"""

def f4(x): 
  return x + 10 * 5

print(f4(3))
"""
53
65
15
Nada
"""

def f5(x): 
  return x * 3

def f6(x): 
  return x + 3

print(f6(f5(3)))
"""
0
3
6
12
Acontece um erro
"""

def f7(y): 
  return y ** y # potenciação: 3 ** 3 == 27
"""
3
6
9
27
Nada
"""

def f8(y): 
  return y + y + y

f8(10)
"""
1000
30
10
Nada
"""

def f9(x, i, j): 
  return i < x and x < j

print(f9(34, 20, 45))
print(f9(55, 55, 56))
"""
True e False
False e False
True e True
False e True
Nada
"""

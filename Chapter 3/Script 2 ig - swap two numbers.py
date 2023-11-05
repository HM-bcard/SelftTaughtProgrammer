Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l = 4
l = 3
d = k=
SyntaxError: incomplete input
k=66
d = l * k
print(d)
198

================================ RESTART: Shell ================================
l = 2
k = 50
def swap(l,k):
    return k/l
print(swap)
SyntaxError: invalid syntax
swap()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    swap()
NameError: name 'swap' is not defined
print swap()
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(swap(l,k)

      2
...       
SyntaxError: incomplete input
>>> print(swap(l,k)
... 
...       2,3
...       
SyntaxError: '(' was never closed
>>> print(swap(l,k))
...       
... 
...       2,3
...       
SyntaxError: multiple statements found while compiling a single statement
>>> SyntaxError: multiple statements found while compiling a single statement
...       
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
================================ RESTART: Shell ================================
>>> def swap():
...     return k/l
... k = 5
SyntaxError: invalid syntax
>>> k = 5
>>> l = 50
>>> def swap():
...     return k/l
... 
>>> 
>>> print(swap())
0.1

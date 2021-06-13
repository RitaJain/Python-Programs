Python 3.6.9 (default, Jan 26 2021, 15:33:00) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> name="rita"
>>> name=1='seema'
SyntaxError: can't assign to literal
>>> name1='seema'
>>> print(name,name1)
rita seema
>>> print(name[0])
r
>>> print(name[0:2])
ri
>>> print(name[-2])
t
>>> name[0]='m'
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    name[0]='m'
TypeError: 'str' object does not support item assignment
>>> name[0].replace='m'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    name[0].replace='m'
AttributeError: 'str' object attribute 'replace' is read-only
>>> names=['tom','rob','sam','jon','tom']
>>> print(names)
['tom', 'rob', 'sam', 'jon', 'tom']
>>> print(name[0])
r
>>> print(names[0])
tom
>>> names[6]='mona'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    names[6]='mona'
IndexError: list assignment index out of range
>>> names.add[6]='mona'
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    names.add[6]='mona'
AttributeError: 'list' object has no attribute 'add'
>>> names.append='mona'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    names.append='mona'
AttributeError: 'list' object attribute 'append' is read-only
>>> names.append()='monna'
SyntaxError: can't assign to function call
>>> names.sort()
>>> print(names)
['jon', 'rob', 'sam', 'tom', 'tom']
>>> names.reverse()
>>> print(names)
['tom', 'tom', 'sam', 'rob', 'jon']
>>> names.count(tom)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    names.count(tom)
NameError: name 'tom' is not defined
>>> names.count('tom')
2
>>> names.index('tom')
0
>>> names.append('rita')
>>> print(names)
['tom', 'tom', 'sam', 'rob', 'jon', 'rita']
>>> names.pop(0)
'tom'
>>> print(names)
['tom', 'sam', 'rob', 'jon', 'rita']
>>> names.clear()
>>> print(names)
[]
>>> for x in range(10):
	print(x)

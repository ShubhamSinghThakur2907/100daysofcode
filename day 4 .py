Python 3.7.4 (v3.7.4:e09359112e, Jul  8 2019, 14:54:52) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## there are basically 2 types of functions in python
>>> ##pre-defined user defined
>>> ##user defined
>>> ## built in function are the functions which can be used by just calling it
>>> ## example of built in functions help() print() input() min()
>>> ##user defined functions these are the functions wich need to be defined before calling it .
>>> def avarage(x,y):
	print("avarage of x & y is :",(x+y)/2)
    avarage(3,4)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> print(avarage(3,4))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(avarage(3,4))
NameError: name 'avarage' is not defined
>>> def avarage(x,y):
	z=(x+y)/2
	return(z)
avarage(4,6)
SyntaxError: invalid syntax
>>> ##an argument is value sent to function during execution
>>> ## recrtion function means a function can also call itself.
>>> #example of recursive function
>>> def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
SyntaxError: invalid syntax
>>> #A lambda function can take any number of arguments, but can only have one expression
>>> #example of lambada function
>>> x = lambda a : a + 10
print(x(5))
SyntaxError: multiple statements found while compiling a single statement
>>> 

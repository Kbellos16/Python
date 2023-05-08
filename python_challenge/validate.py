# The aim of this challenge is to write code that can analyze code submissions.
# We'll simplify things a lot to not make this too hard.
# Write a function named validate that takes code represented as a string as its only parameter.
# Your function should check a few things:
# the code must contain the def keyword
# otherwise return "missing def"
# the code must contain the : symbol
# otherwise return "missing :"
# the code must contain ( and ) for the parameter list
# otherwise return "missing paren"
# the code must not contain ()
# otherwise return "missing param"
# the code must contain four spaces for indentation
# otherwise return "missing indent"
# the code must contain validate
# otherwise return "wrong name"
# the code must contain a return statement
# otherwise return "missing return"
# If all these conditions are satisfied, your code should return True.

# Here comes the twist: your solution must return True when validating itself.
def validate(a):
    if "def" not in a:
        return "missing def"
    elif ':' not in a:
        return 'missing :'
    elif '(' not in a and ')' not in a:
        return 'missing paren'
    elif '( )' in a and '\'()\'' not in a:
        return "missing param"
    elif '\n ' not in a:
        return 'missing indent'
    elif 'validate' not in a:
        return 'wrong name'
    elif 'return' not in a:
        return 'missing return'
    else:
        return True

b='def foo():\n print(123)'
a="def validate (a):"\
"   if 'def'not in a:"\
"return 'missing def'"

print(validate(('def validate(a):\n if "def" not in a:\n return "missing def"\n elif \':\' not in a:\n return \'missing :\'\n elif \'(\' not in a and \')\' not in a:\n return \'missing paren\'\n elif \'()\' in a:\n return "missing param"\n elif \' \' not in a:\n return \'missing indent\'\n elif \'validate\' not in a:\n return \'wrong name\'\n elif \'return\' not in a:\n return \'missing return\'\n else:\n return True')))
#print (validate(('def foo(x):\nprint(123)')))
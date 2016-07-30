from collections import deque

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")




i=256*256
print('The value of i is', i)

x=42#int(input("Please enter an integer: "))

if x<0:
    x=0
    print('Negative changed to zero')
elif x==0:
    print('Zero')
elif x==1:
    print('Single')
else:
    print('More')

words=['cat','window','defenestrate']
for w in words:
    print(w,len(w))

def ask_ok(prompt, retires=4, reminder='Please try again!'):
    while True:
        ok = 'y'#input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retires = retires - 1
        if retires < 0:
            raise ValueError('invalid user response')
        print(reminder)
ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


i=5
def f(arg=i):
    print(arg)

i=6
f()

def parrot(voltage, state='a stiff', action='voom'):
    print("--This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- It's", state, "!")

parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')
parrot(action='VOOOOOM', voltage=1000000)
parrot('a million', 'bereft of life', 'jump')
parrot('a thousand', state='pushing up the daisies')

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print('-'*40)
    keys=sorted(keywords.keys())
    for kw in keys:
        print(kw,":",keywords[kw])

cheeseshop("Limburger","It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def write_multiple_items(file,separator,*args):
    file.write(separator.join(args))

def concat(*args,sep="/"):
    return sep.join(args)

print(concat("earth","mars","venus"))
concat("earth","mars","venus",sep=".")

list(range(3,6))
args=[3,6]
list(range(*args))

d={"voltage":"four million","state":"bleedin' demised","action":"VOOM"}
parrot(**d)

def make_incrementor(n):
    return lambda x:x+n
f=make_incrementor(42)
print(f(0))
print(f(1))

pairs=[(1,'one'),(2,'two'),(3,'three'),(4,'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anythind.
    """
    pass
print(my_function.__doc__)

def f(ham: str, eggs: str = 'eggs')->str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham+' and '+eggs
f('spam')





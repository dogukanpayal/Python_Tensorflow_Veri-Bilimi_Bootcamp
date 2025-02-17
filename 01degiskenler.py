isim = input()
print("Merhaba "+ isim)

a=24
def f():
    print(a)
f()
def g():
    global a
    a=9
    print(a)
g()
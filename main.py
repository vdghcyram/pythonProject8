def f():
    a = dict()
    _s = input()
    while _s != '':
        s = _s.split()
        a[s[0] + ' ' + s[1]] = int(s[2])
        _s = input()
    return a

count = int(input())
list = []

for i in range(count):
    list.append(f())

for j in list:
    print(j)

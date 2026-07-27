s = set()
s.add(18)
s.add("18")
print(s)

p = set()
p.add(20)
p.add(20.0)
p.add('20')
print(p)
print(len(p))

q ={}
print(type(q))
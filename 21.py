from fractions import Fraction
from sys import stdin

# Part 1
# dict of functions
make_fn = lambda e: lambda: e[0] if len(e)==1 else F"({m[e[0]]()}{e[1]}{m[e[2]]()})"
(m:={s[:4]: make_fn(s[6:].split()) for s in stdin})
print(eval(m['root']()))

# Part 2
# (m:={s[:4]:(lambda e:lambda:len(e)<9 and 'Fraction(%s)'%e or '(%s%s%s)'%(m[e[:4]](),e[5],m[e[7:11]]()))(s[:4]=='root' and s[6:11]+'-'+s[12:] or s[6:-1]) for s in stdin.readlines()}) and (t:=[m.update({'humn':(lambda:x)}) or eval(m['root']()) for x in [0,1]]) and print(t[0]/(t[0]-t[1]))

from sys import stdin

#(s:=stdin.read()) and print(next(i+4 for i in range(len(s)) if len(set(s[i:i+4]))==4))
(s:=stdin.read()) and print(next(i+14 for i in range(len(s)) if len(set(s[i:i+14]))==14))

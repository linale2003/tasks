s= [1,2,3,4,5]
s.insert(0,s[len(s)-1])
s.insert(len(s),s[1])
s.pop(1)
s.pop(len(s)-2)
print(s)
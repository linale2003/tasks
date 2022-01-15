s=int(input())
def f(s):
    if s==-0 or s==1 :
        return 1
    else:
        return s*f(s-1)


print(f(s))
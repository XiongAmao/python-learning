'''
type()
float() integer/float -> float
str()
chr() integer -> char
ord() # string of length 1 or a char -> int
'''
def logType(val=None):
    if val is None :
        return
    print('type is :', type(val))
    print('val is :', val)
    print('--------')

a = 100
b = 1.213
c = 1 + 5j
d = 'yes we can'
e = True
# f = float(d)    could not convert string to float: 'yes we can'
# g = float(c)    can't convert complex to float
h = str(c)   
# i = chr(b)      interger argument expected, got float
# j = ord(a)      expected string of length 1, but int found
# k = ord(b)      expected string of length 1, but float found
# l = ord(d)      expected a character, but string of length 10 found
n = ord('f')
m = ord('帅')
# o = chr(d)      an integer is required(got type str)

logType(a)
logType(b)
logType(c)
logType(d)
logType(e)
# logType(f)
# logType(g)
logType(h)
# logType(i)
# logType(j)
# logType(k)
# logType(l)
logType(n)
logType(m)
# logType(o)

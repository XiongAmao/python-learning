'''
how to use operator
'''
def p(p):
    print(p)

a = 5
b = 10 
c = 3 
d = 4
e = 5

a += b
p('a = {0}'.format(a))
a -= c
p('a = {0}'.format(a))
a *= d
p('a = {0}'.format(a))
a /= e
p('a = {0}'.format(a))

p('-----------')
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 and flag1
flag5 = flag1 or flag2
flag6 = not flag1
p('flag1 = 3 > 2')
p('flag2 = 2 < 1')
p('')
p('flag1 = {}'.format(flag1))
p('flag2 = {}'.format(flag2))
p('flag1 and flag2: {}'.format(flag3))
p('flag1 and flag1: {}'.format(flag4))
p('flag1 or flag2: {}'.format(flag5))
p('not flag1: {}'.format(flag6))

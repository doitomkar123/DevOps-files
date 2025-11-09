print("Hello World")

# data type
# primitive - int float boolean string
# non primitive - list, dict, set, tuple

a = -1
print(a)


b = 0.1
print(b)

c = 'abcd'
print(c)

d = True
print(d)


l = ['abcd', 1, -1, '11']
print(l)

print(type(l))


# if loop

# for loop

# while


if a == 1:
    print('yes')
else:
    print('No')


for i in range(10,0,-1):
    print(i)
print("-----------")

ab = 1
while ab < 10:
    print(ab)
    ab = ab+1


for i in l:
    print(i)


seta = {1,2,3,4,5,1}
print(seta)
print(type(seta))

tupa = (1,2,3,4,5)
print(tupa)
print(type(tupa))

l.append('new')
l[0] = 45
print(l)

# tupa[0] = 45
print(tupa)


d = {1:"one", 2:"two", 3:"three"}
print(d)
print(type(d))
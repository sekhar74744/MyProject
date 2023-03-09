## conditional control statements ##

# 1) IF:

print('############## (1)IF #################')

a = 10
b = 20
if a < b:
    print("a is smaller")
print("done") 

# 2) IF_ELSE:

print('############## (2)IF_ELSE #################')
    

a = 30 
b = 20
if a < b:
    print("a is smaller")
else:
	print("b is smaller")
 

 
# 3) IF_ELSE_LADDER:

print('############## (3)IF_ELSE_LADDER #################')

a = 10 
b = 20
if a > b:
	print("a is smaller")
elif b < a:
	print("b is bigger")
else:
	print("a & b are not equal")


##multable
print('############## multable #################')

n = 20
for i in range(1, 11):
	print(n, 'x', i, '=', n*i )

print('############## multable #################')

for i in range(1,21):
	print("\n\nmul table for %d\n" %(i))
	for j in range(1, 11):
		print("%-5d x %5d = %5d" % (i, j, i*j))

for i in range(1,8):
	print("\n\nmul table for %d\n" %(i))
	for j in range(1, 11):
		print("%d x %d = %d" %(i, j, i*j))




print('############## multable #################')

l = [1, 2, 3, 4, 5]
print(l[0] *2)
print(l[1] *2)
print(l[2] *2)
print(l[3] *2)
print(l[4] *2)

print("##########' * for loop * '###########" )

l = [1, 2, 3, 4, 5]
for i in l:
	print(i)
	print(i * 2)
print(i)
print("i am outside of for loop")

l = [1, 2, 3, 4, 5]
for i in l:
	if i % 2 == 0:
		print(i)

l = [1, 2, 3, 4, 5]
for i in l:
	if i % 2 == 0:
		print(i)
	else:
		print(i * 2)

		

print("##########' * append * '###########" )

l1 = [1, 2, 3, 4, 5]
s = []
for i in l1:
	print(i)
	s.append(str(i))
print(s)


print("##########' * extend * '###########" )


l1 = [1, 2, 3, 4, 5]
s = []
for i in l1:
	print(i) 
	s.extend(str(i))
print(s)


print("##########' * insert * '###########" )


l1 = [1, 2, 3, 4, 5]
s = []
for i in l1:
	print(i)
	s.insert(5,str(i))
print(s)

print("##########' * break * '###########" )

l = [1, 2, 3, 4, 5]
ele = 3
for i in l:
	if i == 3:
		print(f'{3} is in list')
		break
print("outside for loop", i)



print("##########' * continue * '###########" )

l = [1, 2, 3, 4, 5]
for i in l:
	print(i)
	print(i*i)
	if i%2 == 0:
		continue
  # print(i**3)
	

print("##########' * while loop * '###########" )

i = 0
while (i < 6):
	print(i)
	i = i+1
print("i am outside in loop")


print("##########' * practice  * '###########" )

c = ["india", "russia", "china", "usa", "pak", "uk"]

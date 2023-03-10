#### practice tasks ####

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

print("##########' * practice  * '###########" )

c = {"india", "russia", "china", "usa", "pak", "uk"}
d = {}
for i in c:
	print(i)
	d[i] = len(i)
print(d)


c = ["india", "russia", "china", "usa", "pak", "uk"]
d = []
for i in c:
	print(i)
	if len(i) > 3:
		d.append(i)
print(d)


c = ["india", "russia", "china", "usa", "pak", "uk"]
d = []
for i in c:
	print(i)
	if len(i) == 3:
		d.insert(3, i)
print(d)




fruits = ('apple','banana','cherry')
print(fruits[0])
fruits = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(fruits[2:5])
print(fruits[:5])
print(fruits[2:])
#เพิ่มค่าในTuple
x = ("apple","banana","cherry")
y = list(x)
y[1]
x = tuple(y)#แปลงlistเป็นtupleแล้วกลับมาค่าที่X

print(x)

x = ("apple","banana","cherry")
y = list(x)
y.remove('apple')
x = tuple(y)
print(x)

tuple1 = ("a","b","c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2
print(tuple3)
x = range(3,6)
for n in x:
    print(n)
x = range(3,20,5)
for n in x:
    print("rangeแบบเสต็ป2")
#นายเจษฎา ทรัพย์วิบูลพงษ์ ม.6/14 เลขที่ 7



























































































































































































































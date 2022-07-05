car = {"brand": "Ford",
    "model": "mustang",
    "year": 1964
}
print(car['brand'])
print(car)
x = car.keys()
print(x)
#เพิ่มค่าในdic
car["color"] = "white"
print(x)
#แก้ค่าในdic
car["color"] = "red"
print(car)
#การอัพเดทdic
car.update({"light": "blue"})
print(car)
#ลบค่าในdic
car.pop("light")
print(car)
del car["color"]
print(car)
#เพิ่มค่าในdicแบบ list
car.update({"part":["body","wheel","light"]})
print(car)
#เพิ่มค่าในdicแบบ Nested
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
 },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
 },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
 }
}
print(myfamily['child1'])
#นายเจษฎา ทรัพย์วิบูลพงษ์ ม.6/14 เลขที่ 7
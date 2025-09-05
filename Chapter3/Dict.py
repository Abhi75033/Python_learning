marks = {
    "Abhishek":100,
    "Alex" : 56,
    "Aditya":90,
    False : "Kela",
    "name":"akhil"
}

print(marks.values())

marks.update({"Abhishek":99,"sampada":100})

print(marks.get('Neha')) # Retuen none 

marks.setdefault("Abhishek",None)

name = marks.setdefault('name', 'Bob')

print(f"Returned value: {name}")
print(f"Dictionary after: {marks}")

print(marks)
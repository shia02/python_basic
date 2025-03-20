#辞書
car = {"brand": "Toyota", "model": "prius", "year": 2015}
print(car.get('brand'))
print(car.keys(),car.values())
print(car.items())

for k, v in car.items():
    print(f'key = {k}, item = {v}')

if "model" in car:
    print("model is exist")

car.update({"country": "Japan"})
print(car)
tmp_car = {"model": "car"}
car.update(tmp_car)
print(car)
car['city'] = "Tokyo"
print(car)
value = car.popitem()
print(car, value)

value = car.pop("brand")
print(car, value)
car.clear()
print(car)
sale1 = {"apple": 10, "orange": 20}
sale2 = {"apple": 10, "lemon": 10}
sale3 = {"apple": 10, "orange": 20, "lemon": 10}
sale = sale1.copy()
for name, count in sale2.items():
    sale[name] = sale.get(name, 0) + count
for name, count in sale3.items():
    sale[name] = sale.get(name, 0) + count
print(sale)

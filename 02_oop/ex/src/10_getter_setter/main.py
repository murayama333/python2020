from mysales.sale import Sale

sale = Sale(800, 10)
sale.set_price(1000)
sale.set_count(20)
sale.print()
print(sale.get_price())
print(sale.get_count())

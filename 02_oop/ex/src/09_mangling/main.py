from mysales.sale import Sale

sale = Sale(800, 10)
sale._Sale__price = 1000
sale._Sale__count = 20
sale.print()
print(sale._Sale__price)
print(sale._Sale__count)

import datetime
from mysales.sale import DailySale

sale = DailySale(800, 10)
sale.print()

date = "2020-10-01"
date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
sale = DailySale(1000, 5, date)
sale.print()

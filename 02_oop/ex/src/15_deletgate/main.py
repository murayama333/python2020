from mysales.sale import Sale, Customer, CustomerSale

customer = Customer("Customer A")
sale = Sale(800, 10)
customer_sale = CustomerSale(customer, sale)
customer_sale.print()

str = "Title: {0} Price: {1:,}"
title = "Python Book"
price = 3000

format_str = str.format(title, price)
print(format_str)

print(f"Title: {title} Price: {price:,}")

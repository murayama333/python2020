book_prices = {"Python Book": 3000, "HTML Book": 1000, "CSS Book": 2000}
title_length = max([len(title) for title in book_prices])
for title, price in book_prices.items():
    print(f"{title:{title_length}}: {price:,}")

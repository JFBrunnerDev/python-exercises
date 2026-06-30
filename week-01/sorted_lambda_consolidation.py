products = [
    {"name": "Widget", "price": 25, "stock": 12},
    {"name": "Gadget", "price": 80, "stock": 3},
    {"name": "Gizmo", "price": 45, "stock": 0},
    {"name": "Doohickey", "price": 15, "stock": 30},
]

price_sorting = sorted(products, key=lambda x: x["price"], reverse=True)
print(price_sorting)

stock_sorting = sorted(products, key=lambda x: x["stock"] if x["stock"] > 0 else float("inf"))
print(stock_sorting)
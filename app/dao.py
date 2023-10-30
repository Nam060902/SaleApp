def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    },{
            "id": 2,
            "name": "Tablet"
    }]

def get_products(kw):
    return [{
        "id": 1,
        "name": "iphone 13",
        "image": "https://cdn.mobilecity.vn/mobilecity-vn/images/2023/04/oppo-find-x6-pro-1.jpg.webp",
        "price": 20000000,
        "categories_id": 1
    },{
        "id": 2,
        "name": "Galaxy pro 13",
        "image": "https://cdn.mobilecity.vn/mobilecity-vn/images/2023/04/oppo-find-x6-pro-1.jpg.webp",
        "price": 22000000,
        "categories_id": 1
    },{
        "id": 3,
        "name": "Tablet pro max",
        "image": "https://cdn.mobilecity.vn/mobilecity-vn/images/2023/04/oppo-find-x6-pro-1.jpg.webp",
        "price": 20000000,
        "categories_id": 2
    },{
        "id": 1,
        "name": "iphone 13",
        "image": "https://cdn.mobilecity.vn/mobilecity-vn/images/2023/04/oppo-find-x6-pro-1.jpg.webp",
        "price": 20000000,
        "categories_id": 1
    },{
        "id": 1,
        "name": "iphone 13",
        "image": "https://cdn.mobilecity.vn/mobilecity-vn/images/2023/04/oppo-find-x6-pro-1.jpg.webp",
        "price": 20000000,
        "categories_id": 1
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
PRODUCTS = [
    {
        "id": 1,
        "name": "Large Coffee",
        "price": 6.00
    },
    {
        "id": 2,
        "name": "Latte",
        "price": 8.99
    },
    {
        "id": 3,
        "name": "Blueberry Muffin",
        "price": 9.49
    },
    {
        "id": 4,
        "name": "Scone",
        "price": 7.56
    },
    {
        "id": 5,
        "name": "Bran Muffin",
        "price": 9.10
    },
    {
        "id": 6,
        "name": "Mocha Latte",
        "price": 12.99
    },
    {
        "id": 7,
        "name": "Espresso",
        "price": 11.80
    },
    {
        "id": 8,
        "name": "Americano",
        "price": 11.00
    },
    {
        "id": 9,
        "name": "Cubano",
        "price": 14.99
    },
    {
        "id": 10,
        "name": "Cappucino",
        "price": 12.49
    }
]


def get_all_products():
    return PRODUCTS


def get_single_product(id):
    # Variable to hold the found size, if it exists
    requested_product = None

    # Iterate the PRODUCTS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for product in PRODUCTS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if product["id"] == id:
            requested_product = product

    return requested_product

products = input('Podaj produkty (oddziel je przecinkiem, nie używaj spacji): ')
try:
    products = products.split(",")
    set_of_products = set()
    for product in products:
        product_without_white_characters = product.strip()
        if(product_without_white_characters):
            set_of_products.add(product_without_white_characters)

    dictionary_of_products = {}
    for product in set_of_products:
        price = float(input('Podaj cenę ' + product + ": "))
        dictionary_of_products.update({product: price})

    for name, price in dictionary_of_products.items():
        print(name + ":" + str(price))
except ValueError:
    print('Podana cena jest niepoprawna')
except Exception as e:
    print('Coś poszło nie tak')
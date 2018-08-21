from data import products_string
from pprint import pprint
from step_1 import transform_products_to_list


def group_products_by_customer_and_invoice(products_string):
    products_list = transform_products_to_list(products_string)

    products = {}

    for product in products_list:
        invoice = product[0]
        customer_id = product[-2]

        products.setdefault(customer_id, {})

        products[customer_id].setdefault(invoice, [])
        products[customer_id][invoice].append(product)

    return products




products = group_products_by_customer_and_invoice(products_string)

customer = products['12583']
# print(customer)
invoice = customer['536370']
# print(invoice)
item = invoice[1]
# print(item)
weird_description = item[2]
# print(weird_description)

alternate_way = products['12583']['536370'][1][2]
print(alternate_way)

pprint(products)

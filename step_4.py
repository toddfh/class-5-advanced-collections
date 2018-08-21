from step_1 import transform_products_to_list
from pprint import pprint


def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    product = {}
    for products in products_list:
        invoice = products[0]
        customer_id = products[-2]
        unit_price = float(products[5])
        quantity = float(products[3])

        total = unit_price * quantity

        product.setdefault(customer_id, {})
        product[customer_id].setdefault(invoice, 0)
        product[customer_id][invoice] += total
        product[customer_id][invoice] = round(product[customer_id][invoice], 2)

    return product

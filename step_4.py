from step_1 import transform_products_to_list


def calculate_total_per_invoices(products_string):
    products_list = transform_products_to_list(products_string)
    product = {}
    for products in products_list:
        invoice = products[0]
        customer_id = products[-2]
        total = float(products[5]) * float(products[3])

        product.setdefault(customer_id, {})
        product[customer_id].setdefault(invoice, 0)
        product[customer_id][invoice] += round(total, 2)

    return product

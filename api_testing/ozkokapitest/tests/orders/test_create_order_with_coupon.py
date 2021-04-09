import pytest
import random
from ozkokapitest.src.helpers.coupon_helper import CouponHelper
from ozkokapitest.src.helpers.product_helper import ProductsHelper
from ozkokapitest.src.helpers.orders_helper import OrdersHelper
from ozkokapitest.src.utilities.generic_utilities import generate_random_string


pytestmark = [pytest.mark.coupon, pytest.mark.order]


@pytest.mark.tcid60
def test_create_order_with_percent_discount():

    # create coupon
    coupon_helper = CouponHelper()
    discount_type = 'percent'
    coupon_amount = random.randint(5, 50)
    generate_code = generate_random_string(
        length=10, prefix=(str(coupon_amount) + "off_"))

    info = {
        "code": generate_code,
        "discount_type": discount_type,
        "amount": str(coupon_amount)
    }
    coupon_rs = coupon_helper.create_coupon(info)

    # create product
    product_price = random.randint(50, 100)
    product_helper = ProductsHelper()
    payload = {}
    payload['name'] = generate_random_string(length=20, prefix="test_")
    payload['type'] = "simple"
    payload['regular_price'] = str(product_price)

    product_rs = product_helper.call_create_product(payload)

    # create order
    order_helper = OrdersHelper()

    customer_id = 0
    product_id = product_rs['id']

    info = {
        "line_items": [
            {
                "product_id": product_id,
                "quantity": 1
            }
        ],
        "coupon_lines": [
            {
                "code": coupon_rs['code']
            }
        ],
        "shipping_lines": [
            {
                "method_id": "flat_rate",
                "method_title": "Flat Rate",
                "total": "0.00"
            }
        ]
    }
    order_json = order_helper.create_order(additional_args=info)

    # verify order price in database correct with the discount amount
    discount_amount = round(float(product_price) *
                            (float(coupon_amount/100)), 2)

    discounted_price = round((float(product_price) - discount_amount), 2)

    assert order_json['discount_total'] == str(discount_amount), \
        f"Order discount amount calculation is incorrect." \
        f"Expected: {discount_amount}" \
        f"Actual: {order_json['discount_total']}"

    assert order_json['total'] == str(discounted_price), \
        f"Order total price calculation is incorrect." \
        f"Expected: {discounted_price}" \
        f"Actual: {order_json['total']}"

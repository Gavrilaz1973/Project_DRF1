import stripe
def session_payment(obj):
    stripe.api_key = "sk_test_51NsMTfBebpZ3azh4TPndIkvzVFEewmKWtyZ5uezetjQTOEY1wYKPy3P06V3ETU9GbjX2Oe2900pCXwhWWYFKzdEk0057cLyjR0"
    prod = stripe.Product.create(name=f'Course payment: {obj}.')
    price = stripe.Price.create(
        unit_amount=1000,
        currency="usd",
        recurring={"interval": "month"},
        product=prod.id,
    )
    response = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="subscription",
    )
    return response.url
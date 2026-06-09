import stripe
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def convert_rub_to_usd(ammount)


def create_stripe_price (amount):
    """Создает цену в страйпе"""
    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        # recurring={"interval": "month"},
        product_data={"name": "Оплата курсов"},
    )

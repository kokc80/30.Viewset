import stripe
from config.settings import STRIPE_API_KEY
from forex_python.converter import CurrencyRates

stripe.api_key = STRIPE_API_KEY

def convert_rub_to_usd(ammount):
    """Конвертиртует рубли в доллары"""

    c = CurrencyRates()
    rate = c.get_rate("RUB", "USD")
    return int(ammount*rate)


def create_stripe_price(amount):
    """Создает цену в страйпе"""

    # price = stripe.Price.create(
    return stripe.Price.create(
        currency="USD",
        unit_amount=amount * 100,
        # recurring={"interval": "month"},
        product_data={"name": "Оплата курсов"},
    )
    # return price

def create_stripe_session( price):
    """Создает сессию на оплату в страйпе"""

    session = stripe.checkout.Session.create(
        success_url = "https://127.0.0.1:8000/",
        line_items = [{"price": price.get("id"), "quantity": 1}],
        mode = "payment",
    )
    return session.get("id"), session.get("url")
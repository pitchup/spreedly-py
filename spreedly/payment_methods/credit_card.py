from payment_method import PaymentMethod
from spreedly.common.fields import Field, IntegerField


class CreditCard(PaymentMethod):
    first_name = Field()
    last_name = Field()
    full_name = Field()
    month = IntegerField()
    year = IntegerField()
    number = Field()
    last_four_digits = Field()
    card_type = Field()
    verification_value = Field()
    address1 = Field()
    address2 = Field()
    city = Field()
    state = Field()
    zip = Field()
    country = Field()
    phone_number = Field()

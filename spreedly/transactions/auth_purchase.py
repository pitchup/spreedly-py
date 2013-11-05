from spreedly.transactions.gateway_transaction import GatewayTransaction
from spreedly.common.fields import Field, IntegerField, BooleanField


class AuthPurchase(GatewayTransaction):
    currency_code = Field()
    amount = IntegerField()
    success = BooleanField()
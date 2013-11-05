from spreedly.common.fields import Fields, Field, BooleanField, DateTimeField
from transaction import Transaction


class Response(Fields):
    success = BooleanField()
    pending = BooleanField()
    cancelled = BooleanField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
    message = Field()
    avs_code = Field()
    avs_message = Field()
    cvv_code = Field()
    cvv_message = Field()
    error_code = Field()
    error_detail = Field()


class GatewayTransaction(Transaction):
    order_id = Field()
    ip = Field()
    description = Field()
    gateway_token = Field()
    merchant_name_descriptor = Field()
    merchant_location_descriptor = Field()
    on_test_gateway = BooleanField()

    # Yup, sub-elements work. Who wants to touch me?
    response = Response()


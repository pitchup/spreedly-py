from spreedly.payment_methods.payment_method import PaymentMethod
from transaction import Transaction


class RedactPaymentMethod(Transaction):
    def __init__(self, xml_doc):
        super(RedactPaymentMethod, self).__init__(xml_doc)
        self.payment_method = PaymentMethod(xml_doc.find('.//payment_method'))

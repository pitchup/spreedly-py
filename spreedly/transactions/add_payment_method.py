from transaction import Transaction
from spreedly.common.fields import BooleanField
from spreedly.payment_methods.payment_method import PaymentMethod


class AddPaymentMethod(Transaction):
    retained = BooleanField()
    payment_method = PaymentMethod()

    def __init__(self, xml_doc):
        #TODO This is pretty similar to the ruby, but can I find a nicer way?
        self.payment_method = PaymentMethod.from_xml(xml_doc.xpath('.//payment_method')[0])
        super(AddPaymentMethod, self).__init__(xml_doc)
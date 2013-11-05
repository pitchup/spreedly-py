from spreedly.model import Model
from spreedly.common.fields import Field
from spreedly.common.error_parser import errors_from


class PaymentMethod(Model):
    email = Field()
    storage_state = Field()
    data = Field()

    @classmethod
    def from_xml(cls, xml_doc):
        from paypal import Paypal
        from credit_card import CreditCard

        payment_method_xml = xml_doc.xpath('.//payment_method_type')[0]

        payment_method = payment_method_xml.text

        if payment_method == 'credit_card':
            return CreditCard(xml_doc)
        elif payment_method == 'paypal':
            return Paypal(xml_doc)
        elif payment_method == 'sprel':
            return Sprel(xml_doc)
        elif payment_method == 'bank_account':
            return BankAccount(xml_doc)

    @classmethod
    def list_from_xml(cls, xml_doc):
        payment_methods = []

        for xml_payment in xml_doc.at_xpath('.//payment_method_type'):
            payment_methods.append(PaymentMethod.from_xml(xml_payment))

        return payment_methods

    #def __init__(self, xml_doc=None):
    #    super(PaymentMethod, self).__init__(xml_doc=xml_doc)
    #
    #    self.errors = errors_from(xml_doc)

    def valid(self):
        return len(self.errors) > 0
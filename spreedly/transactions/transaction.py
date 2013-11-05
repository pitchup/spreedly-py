from spreedly.model import Model
from spreedly.common.fields import Field, BooleanField


class Transaction(Model):
    state = Field()
    message = Field()
    succeeded = BooleanField()

    @classmethod
    def from_xml(cls, xml_doc):
        from add_payment_method import AddPaymentMethod
        from purchase import Purchase
        from retain_payment_method import RetainPaymentMethod
        from redact_payment_method import RedactPaymentMethod

        transaction_type = xml_doc.xpath('.//transaction_type')[0].text

        if transaction_type == 'AddPaymentMethod':
            return AddPaymentMethod(xml_doc)
        elif transaction_type == 'Purchase':
            return Purchase(xml_doc)
        elif transaction_type == 'Authorization':
            #return Authorization.from_xml(xml_doc)
            pass
        elif transaction_type == 'Capture':
            #return Capture.from_xml(xml_doc)
            pass
        elif transaction_type == 'Credit':
            #return Refund.from_xml(xml_doc)
            pass
        elif transaction_type == 'Void':
            #return Void.from_xml(xml_doc)
            pass
        elif transaction_type == 'RetainPaymentMethod':
            return RetainPaymentMethod(xml_doc)
        elif transaction_type == 'RedactPaymentMethod':
            return RedactPaymentMethod(xml_doc)
        elif transaction_type == 'RedactGateway':
            return RedactGateway(xml_doc)
        else:
            #TODO Need to understand what is happening here.
            pass

    @classmethod
    def list_from_xml(cls, xml_doc):
        for xml_transaction in xml_doc.at_xpath('.//payment_method_type'):
            Transaction.append(Transaction.from_xml(xml_transaction))




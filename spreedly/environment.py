import ssl_requester
import urls
import base64
from lxml.builder import E
from lxml import etree
from payment_methods.payment_method import PaymentMethod
from transactions.transaction import Transaction
from gateway import Gateway


class Environment(object):
    def __init__(self, environment_key, access_secret, options=None):
        options = options or {}

        self.key = environment_key
        self.access_secret = environment_key, access_secret
        self.base_url = options.get('base_url', 'https://core.spreedly.com')
        self.currency_code = options.get('currency_code', 'USD')
        self.headers = self._init_headers()

    def transparent_redirect_form_action(self):
        return "%s/v1/payment_methods" % self.base_url

    def find_payment_method(self, token):
        xml_doc = ssl_requester.ssl_get(urls.find_payment_method_url(token), self.headers)
        return PaymentMethod.from_xml(xml_doc)

    def find_transaction(self, transaction_token):
        xml_doc = ssl_requester.ssl_get(urls.find_transaction_url(transaction_token), self.headers)
        return Transaction.from_xml(xml_doc)

    def find_transcript(self, transcription_token):
        ssl_requester.ssl_raw_get(urls.find_transaction_url(transcription_token), self.headers)

    def find_gateway(self, token):
        xml_doc = ssl_get(find_gateway_url(token), self.headers)
        return Gateway(xml_doc)

    def purchase_on_gateway(self, gateway_token, payment_method_token, amount, options=None):
        auth_purchase = self.auth_purchase_body(amount, payment_method_token, options)

        return self.api_post(urls.purchase_url(gateway_token), auth_purchase)

    def auth_purchase_body(self, amount, payment_method_token, options):
        auth_purchase = (
            E.transaction(
                E.amount(str(amount)),
                E.currency_code(options.get('currency_code', 'USD')),
                E.payment_method_token(payment_method_token)
            )
        )

        self.add_to_doc(auth_purchase, options)

        return auth_purchase

    def add_credit_card(self, card_details):
        credit_card = self.credit_card_body(card_details)

        return self.api_post(urls.add_gateway_url(), credit_card, False)

    def credit_card_body(self, options):
        payment_method = etree.Element('payment_method')

        self.add_to_doc(payment_method, options, ('data', 'retained', 'email',))

        credit_card = etree.SubElement(payment_method, 'credit_card')

        self.add_to_doc(credit_card, options, ('number', 'month', 'first_name', 'last_name', 'year', 'address1',
                                               'address2', 'city', 'state', 'zip', 'country', 'phone_number',))

        return payment_method

    def add_gateway(self, gateway_type, credentials=None):
        credentials = credentials or {}
        
        body = self.add_gateway_body(gateway_type, credentials)
        xml_doc = ssl_requester.ssl_post(urls.add_gateway_url(), body, self.headers)

        return Gateway(xml_doc)

    def add_gateway_body(self, gateway_type, credentials):
        gateway = etree.Element('gateway')
        etree.SubElement(gateway, 'gateway_type').text = gateway_type

        #TODO Ruby code passes in all of the credential keys here.
        self.add_to_doc(gateway, credentials)
        
        return gateway

    def add_to_doc(self, xml_doc, options, attributes=None):
        if not attributes:
            attributes = options.iterkeys()

        for k in attributes:
            if k in options:
                element = etree.SubElement(xml_doc, k)
                element.text = options[k]

    def api_post(self, url, body, talking_to_gateway=True):
        xml_doc = ssl_requester.ssl_post(url, body, self.headers, talking_to_gateway)
        return Transaction.from_xml(xml_doc)

    def _init_headers(self):
        return {
            'Authorization': 'Basic ' + base64.b64encode('%s:%s' % (self.key, self.access_secret)),
            'Content-Type': 'text/xml'
        }








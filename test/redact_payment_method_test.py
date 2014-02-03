import unittest
from lxml import etree
from mock import patch

from spreedly.environment import Environment
from spreedly.transactions.redact_payment_method import RedactPaymentMethod


class TestRedactPaymentMethod(unittest.TestCase):
    def setUp(self):
        self.environment = Environment("key", "secret")

    @patch('spreedly.environment.ssl_requester.raw_ssl_request')
    def test_successful_redact(self, test_patch):
        request_mock = test_patch.return_value
        request_mock.status_code = 200
        request_mock.text = successful_redact_response

        transaction = self.environment.redact_payment_method(
            "TransactionToken", {'remove_from_gateway': 'ThePassedGatewayToken'})
        self.assertIsInstance(transaction, RedactPaymentMethod)

        self.assertEqual(transaction.token, '2BSe5T6FHpypph3ensF7m3Nb3qk')
        self.assertEqual(transaction.created_at.year, 2013)
        self.assertEqual(transaction.created_at.month, 8)
        self.assertEqual(transaction.created_at.day, 05)
        self.assertEqual(transaction.message, 'Succeeded!')
        self.assertEqual(transaction.state, 'succeeded')
        self.assertEqual(transaction.payment_method.storage_state, 'redacted')
        self.assertEqual(transaction.payment_method.token, 'RvsxKgbAZBmiZHEPhhTcOQzJeC2')

    def test_redact_payment_method_body(self):
        body = self.environment.redact_payment_method_body({'remove_from_gateway': 'ThePassedGatewayToken'})
        print etree.tostring(body)

        transaction = body.xpath('.')[0]
        self.assertEqual(transaction.xpath('./remove_from_gateway')[0].text, 'ThePassedGatewayToken')


successful_redact_response = """
      <transaction>
        <on_test_gateway type="boolean">false</on_test_gateway>
        <created_at type="datetime">2013-08-05T17:43:41Z</created_at>
        <updated_at type="datetime">2013-08-05T17:43:41Z</updated_at>
        <succeeded type="boolean">true</succeeded>
        <token>2BSe5T6FHpypph3ensF7m3Nb3qk</token>
        <state>succeeded</state>
        <gateway_specific_fields nil="true"/>
        <gateway_specific_response_fields nil="true"/>
        <transaction_type>RedactPaymentMethod</transaction_type>
        <order_id nil="true"/>
        <ip nil="true"/>
        <message key="messages.transaction_succeeded">Succeeded!</message>
        <payment_method>
          <token>RvsxKgbAZBmiZHEPhhTcOQzJeC2</token>
          <created_at type="datetime">2013-08-05T17:43:41Z</created_at>
          <updated_at type="datetime">2013-08-05T17:43:41Z</updated_at>
          <email>perrin@wot.com</email>
          <data nil="true"/>
          <storage_state>redacted</storage_state>
          <last_four_digits>4444</last_four_digits>
          <card_type>master</card_type>
          <first_name>Perrin</first_name>
          <last_name>Aybara</last_name>
          <month type="integer">1</month>
          <year type="integer">2019</year>
          <address1 nil="true"/>
          <address2 nil="true"/>
          <city nil="true"/>
          <state nil="true"/>
          <zip nil="true"/>
          <country nil="true"/>
          <phone_number nil="true"/>
          <full_name>Perrin Aybara</full_name>
          <payment_method_type>credit_card</payment_method_type>
          <errors>
          </errors>
          <verification_value></verification_value>
          <number>XXXX-XXXX-XXXX-4444</number>
        </payment_method>
      </transaction>
"""
import unittest
from mock import patch

from spreedly.environment import Environment
from spreedly.transactions.purchase import Purchase


class TestPurchase(unittest.TestCase):
    def setUp(self):
        self.environment = Environment("key", "secret")

    @patch('spreedly.environment.ssl_requester.raw_ssl_request')
    def test_successful_purchase_on_gateway(self, test_patch):
        request_mock = test_patch.return_value
        request_mock.status_code = 200
        request_mock.text = successful_purchase_response

        transaction = self.environment.purchase_on_gateway("TheGatewayToken", "TheCardToken", 2001, all_possible_options)
        self.assertIsInstance(transaction, Purchase)

        self.assertEqual(transaction.amount, 144)
        self.assertEqual(transaction.token, 'Btcyks35m4JLSNOs9ymJoNQLjeX')
        self.assertEqual(transaction.created_at.year, 2013)
        self.assertEqual(transaction.created_at.month, 7)
        self.assertEqual(transaction.created_at.day, 31)
        self.assertEqual(transaction.response.error_detail, 'The eagle lives!')
        self.assertEqual(transaction.response.message, 'Successful purchase')

    @patch('spreedly.environment.ssl_requester.raw_ssl_request')
    def test_failed_purchase_on_gateway(self, test_patch):
        request_mock = test_patch.return_value
        request_mock.status_code = 200
        request_mock.text = failed_purchase_transaction

        transaction = self.environment.purchase_on_gateway("TheGatewayToken", "TheCardToken", 2001, all_possible_options)
        self.assertIsInstance(transaction, Purchase)

        self.assertEqual(transaction.amount, 5148)
        self.assertEqual(transaction.token, 'RxkxK78ZlvDiXRQRnyuJM5ee0Ww')
        self.assertEqual(transaction.created_at.year, 2013)
        self.assertEqual(transaction.created_at.month, 7)
        self.assertEqual(transaction.created_at.day, 31)
        self.assertFalse(transaction.success)
        self.assertEqual(transaction.state, 'gateway_processing_failed')
        self.assertEqual(transaction.response.error_detail, 'The eagle is dead Jim.')

    def test_auth_purchase_body(self):
        body = self.environment.auth_purchase_body(100, "TheCardToken", all_possible_options)

        self.assertEqual(int(body.xpath('./amount')[0].text), 100)
        self.assertEqual(body.xpath('./currency_code')[0].text, 'EUR')
        self.assertEqual(body.xpath('./retain_on_success')[0].text, 'true')


all_possible_options = {
    "currency_code": "EUR",
    "order_id": "8675",
    "description": "SuperDuper",
    "ip": "183.128.100.103",
    "merchant_name_descriptor": "Real Stuff",
    "merchant_location_descriptor": "Raleigh",
    "retain_on_success": 'true'
}

successful_purchase_response = """
      <transaction>
        <amount type="integer">144</amount>
        <on_test_gateway type="boolean">true</on_test_gateway>
        <created_at type="datetime">2013-07-31T19:46:26Z</created_at>
        <updated_at type="datetime">2013-07-31T19:46:32Z</updated_at>
        <currency_code>USD</currency_code>
        <succeeded type="boolean">true</succeeded>
        <state>succeeded</state>
        <token>Btcyks35m4JLSNOs9ymJoNQLjeX</token>
        <transaction_type>Purchase</transaction_type>
        <order_id>187A</order_id>
        <ip nil="true"/>
        <description>4 Shardblades</description>
        <merchant_name_descriptor nil="true"/>
        <merchant_location_descriptor nil="true"/>
        <gateway_specific_fields nil="true"/>
        <gateway_specific_response_fields nil="true"/>
        <message key="messages.transaction_succeeded">Succeeded!</message>
        <gateway_token>YOaCn5a9xRaBTGgmGAWbkgWUuqv</gateway_token>
        <response>
          <success type="boolean">true</success>
          <message>Successful purchase</message>
          <avs_code>22</avs_code>
          <avs_message nil="true">I will be back</avs_message>
          <cvv_code>31</cvv_code>
          <cvv_message nil="true">Rutabaga</cvv_message>
          <pending type="boolean">false</pending>
          <error_code>899</error_code>
          <error_detail nil="true">The eagle lives!</error_detail>
          <cancelled type="boolean">false</cancelled>
          <created_at type="datetime">2013-07-31T19:46:26Z</created_at>
          <updated_at type="datetime">2013-07-31T19:46:27Z</updated_at>
        </response>
        <payment_method>
          <token>8xXXIPGXTaPXysDA5OUpgnjTEjK</token>
          <created_at type="datetime">2013-07-31T19:46:25Z</created_at>
          <updated_at type="datetime">2013-07-31T19:46:26Z</updated_at>
          <email>perrin@wot.com</email>
          <data nil="true"/>
          <storage_state>retained</storage_state>
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
        <api_urls>
        </api_urls>
      </transaction>
"""

failed_purchase_transaction = """
      <transaction>
        <amount type="integer">5148</amount>
        <on_test_gateway type="boolean">true</on_test_gateway>
        <created_at type="datetime">2013-07-31T19:51:57Z</created_at>
        <updated_at type="datetime">2013-07-31T19:51:57Z</updated_at>
        <currency_code>USD</currency_code>
        <succeeded type="boolean">false</succeeded>
        <state>gateway_processing_failed</state>
        <token>RxkxK78ZlvDiXRQRnyuJM5ee0Ww</token>
        <transaction_type>Purchase</transaction_type>
        <order_id nil="true"/>
        <ip nil="true"/>
        <description nil="true"/>
        <merchant_name_descriptor nil="true"/>
        <merchant_location_descriptor nil="true"/>
        <gateway_specific_fields nil="true"/>
        <gateway_specific_response_fields nil="true"/>
        <message>Unable to process the purchase transaction.</message>
        <gateway_token>Y6jMbUCm2oz6QTpavzp0xLaV9mk</gateway_token>
        <response>
          <success type="boolean">false</success>
          <message>Unable to process the purchase transaction.</message>
          <avs_code nil="true"/>
          <avs_message nil="true"/>
          <cvv_code nil="true"/>
          <cvv_message nil="true"/>
          <pending type="boolean">false</pending>
          <error_code></error_code>
          <error_detail nil="true">The eagle is dead Jim.</error_detail>
          <cancelled type="boolean">false</cancelled>
          <created_at type="datetime">2013-07-31T19:51:57Z</created_at>
          <updated_at type="datetime">2013-07-31T19:51:57Z</updated_at>
        </response>
        <payment_method>
          <token>H0kioCnUZ8YbQ9rhqJv6zyav01Q</token>
          <created_at type="datetime">2013-07-31T19:51:57Z</created_at>
          <updated_at type="datetime">2013-07-31T19:51:57Z</updated_at>
          <email>perrin@wot.com</email>
          <data nil="true"/>
          <storage_state>retained</storage_state>
          <last_four_digits>1881</last_four_digits>
          <card_type>visa</card_type>
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
          <number>XXXX-XXXX-XXXX-1881</number>
        </payment_method>
        <api_urls>
        </api_urls>
      </transaction>
"""

if __name__ == '__main__':
    unittest.main()











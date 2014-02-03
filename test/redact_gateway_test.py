import unittest
from mock import patch

from spreedly.environment import Environment
from spreedly.transactions.redact_gateway import RedactGateway


class TestRedactGateway(unittest.TestCase):
    def setUp(self):
        self.environment = Environment("key", "secret")

    @patch('spreedly.environment.ssl_requester.raw_ssl_request')
    def test_successful_redact(self, test_patch):
        request_mock = test_patch.return_value
        request_mock.status_code = 200
        request_mock.text = successful_redact_gateway_response

        transaction = self.environment.redact_gateway("TransactionToken")
        self.assertIsInstance(transaction, RedactGateway)

        self.assertEqual(transaction.token, 'NXKt1iNkIJhzF5QCDt1qSsuFbcN')
        self.assertEqual(transaction.created_at.year, 2013)
        self.assertEqual(transaction.created_at.month, 8)
        self.assertEqual(transaction.created_at.day, 19)
        self.assertTrue(transaction.succeeded)
        self.assertEqual(transaction.gateway.token, '8zy49qcEUigjYbpPKCjlhDzUqJ')
        self.assertEqual(transaction.message, 'Succeeded!')
        self.assertEqual(transaction.gateway.name, 'Spreedly Test')
        self.assertEqual(transaction.gateway.state, 'redacted')


successful_redact_gateway_response = """
      <transaction>
        <token>NXKt1iNkIJhzF5QCDt1qSsuFbcN</token>
        <created_at type="datetime">2013-08-19T17:16:07Z</created_at>
        <updated_at type="datetime">2013-08-19T17:16:07Z</updated_at>
        <succeeded type="boolean">true</succeeded>
        <transaction_type>RedactGateway</transaction_type>
        <message key="messages.transaction_succeeded">Succeeded!</message>
        <gateway>
          <token>8zy49qcEUigjYbpPKCjlhDzUqJ</token>
          <gateway_type>test</gateway_type>
          <name>Spreedly Test</name>
          <characteristics>
            <supports_purchase type="boolean">true</supports_purchase>
            <supports_authorize type="boolean">true</supports_authorize>
            <supports_capture type="boolean">true</supports_capture>
            <supports_credit type="boolean">true</supports_credit>
            <supports_void type="boolean">true</supports_void>
            <supports_reference_purchase type="boolean">true</supports_reference_purchase>
            <supports_purchase_via_preauthorization type="boolean">true</supports_purchase_via_preauthorization>
            <supports_offsite_purchase type="boolean">true</supports_offsite_purchase>
            <supports_offsite_authorize type="boolean">true</supports_offsite_authorize>
            <supports_3dsecure_purchase type="boolean">true</supports_3dsecure_purchase>
            <supports_3dsecure_authorize type="boolean">true</supports_3dsecure_authorize>
            <supports_store type="boolean">true</supports_store>
            <supports_remove type="boolean">true</supports_remove>
          </characteristics>
          <state>redacted</state>
          <payment_methods>
            <payment_method>credit_card</payment_method>
            <payment_method>sprel</payment_method>
            <payment_method>third_party_token</payment_method>
            <payment_method>bank_account</payment_method>
          </payment_methods>
          <gateway_specific_fields/>
          <redacted type="boolean">true</redacted>
          <created_at type="datetime">2013-08-19T17:16:06Z</created_at>
          <updated_at type="datetime">2013-08-19T17:16:07Z</updated_at>
        </gateway>
      </transaction>
"""
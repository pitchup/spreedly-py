import unittest
from mock import patch
from spreedly.environment import Environment


class TestAddGateway(unittest.TestCase):
    def setUp(self):
        self.environment = Environment("key", "secret")


    @patch('spreedly.environment.ssl_requester.raw_ssl_request')
    def test_successful_add_gateway(self, test_patch):
        request_mock = test_patch.return_value
        request_mock.status_code = 200
        request_mock.text = successful_add_test_gateway_response

        gateway = self.environment.add_gateway('test')

        self.assertEqual("4dFb93AiRDEJ18MS9xDGMyu22uO", gateway.token)
        self.assertEqual("test", gateway.gateway_type)
        self.assertEqual("retained", gateway.state)
        self.assertEqual("Test", gateway.name)
        self.assertEqual([], gateway.credentials)

    def test_request_body_params(self):
        body = self.environment.add_gateway_body('wirecard', {
            'username': 'TheUsername',
            'password': 'ThePassword',
            'business_case_signature': 'TheSig'
        })

        gateway = body.xpath('/gateway')[0]
        self.assertEqual(gateway.xpath('./gateway_type')[0].text, 'wirecard')
        self.assertEqual(gateway.xpath('./username')[0].text, 'TheUsername')
        self.assertEqual(gateway.xpath('./password')[0].text, 'ThePassword')
        self.assertEqual(gateway.xpath('./business_case_signature')[0].text, 'TheSig')

successful_add_test_gateway_response = """
      <gateway>
        <token>4dFb93AiRDEJ18MS9xDGMyu22uO</token>
        <gateway_type>test</gateway_type>
        <name>Test</name>
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
        <state>retained</state>
        <payment_methods>
          <payment_method>credit_card</payment_method>
          <payment_method>sprel</payment_method>
          <payment_method>third_party_token</payment_method>
          <payment_method>bank_account</payment_method>
        </payment_methods>
        <gateway_specific_fields/>
        <redacted type="boolean">false</redacted>
        <created_at type="datetime">2013-07-31T17:17:36Z</created_at>
        <updated_at type="datetime">2013-07-31T17:17:36Z</updated_at>
      </gateway>
"""

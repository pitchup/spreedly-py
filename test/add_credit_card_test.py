import unittest
from mock import patch

from spreedly.environment import Environment


class TestAddCreditCard(unittest.TestCase):
    def setUp(self):
        self.environment = Environment("key", "secret")

    @patch('spreedly.environment.ssl_requester.raw_ssl_request')
    def test_successful_add_credit_card(self, test_patch):
        request_mock = test_patch.return_value
        request_mock.status_code = 200
        request_mock.text = successful_add_credit_card_response

        transaction = self.environment.add_credit_card(full_card_details)

        self.assertEqual('6wxjN6HcDik8e3mAhBaaoVGSImH', transaction.token)
        self.assertFalse(transaction.retained)
        self.assertTrue(transaction.succeeded)

        self.assertEqual(transaction.created_at.year, 2013)
        self.assertEqual(transaction.created_at.month, 8)
        self.assertEqual(transaction.created_at.day, 2)

        self.assertEqual(transaction.payment_method.token, 'AXaBXfVUqhaGMg8ytf8isiMAAL9')
        self.assertEqual(transaction.payment_method.full_name, 'Eland Venture')
        self.assertEqual(transaction.payment_method.data,
                         "Don't test everything here, since find_payment_method tests it all.")

    def test_auth_purchase_body(self):
        from lxml import etree

        body = self.environment.credit_card_body(full_card_details).xpath('/payment_method')[0]

        self.assertEqual(body.xpath('./data')[0].text, 'talent: Late')
        self.assertEqual(body.xpath('./email')[0].text, 'leavenworth@free.com')
        self.assertEqual(body.xpath('./retained')[0].text, 'true')

        card = body.xpath('./credit_card')[0]

        self.assertEqual(card.xpath('./first_name')[0].text, 'Leavenworth')
        self.assertEqual(card.xpath('./last_name')[0].text, 'Smedry')
        self.assertEqual(card.xpath('./number')[0].text, '9555555555554444')
        self.assertEqual(card.xpath('./month')[0].text, '3')
        self.assertEqual(card.xpath('./year')[0].text, '2021')
        self.assertEqual(card.xpath('./address1')[0].text, '10 Dragon Lane')
        self.assertEqual(card.xpath('./address2')[0].text, 'Suite 9')
        self.assertEqual(card.xpath('./city')[0].text, 'Tuki Tuki')
        self.assertEqual(card.xpath('./state')[0].text, 'Mokia')
        self.assertEqual(card.xpath('./zip')[0].text, '1122')
        self.assertEqual(card.xpath('./country')[0].text, 'Free Kingdoms')
        self.assertEqual(card.xpath('./phone_number')[0].text, '81Ab')


full_card_details = {
    'email': 'leavenworth@free.com',
    'number': '9555555555554444',
    'month': '3',
    'year': '2021',
    'last_name': 'Smedry',
    'first_name': 'Leavenworth',
    'data': "talent: Late",
    'address1': '10 Dragon Lane',
    'address2': 'Suite 9',
    'city': 'Tuki Tuki',
    'state': 'Mokia',
    'zip': '1122',
    'country': 'Free Kingdoms',
    'phone_number': '81Ab',
    'retained': 'true'
}

successful_add_credit_card_response = """
      <transaction>
        <token>6wxjN6HcDik8e3mAhBaaoVGSImH</token>
        <created_at type="datetime">2013-08-02T18:04:45Z</created_at>
        <updated_at type="datetime">2013-08-02T18:04:45Z</updated_at>
        <succeeded type="boolean">true</succeeded>
        <transaction_type>AddPaymentMethod</transaction_type>
        <retained type="boolean">false</retained>
        <message key="messages.transaction_succeeded">Succeeded!</message>
        <payment_method>
          <token>AXaBXfVUqhaGMg8ytf8isiMAAL9</token>
          <created_at type="datetime">2013-08-02T18:04:45Z</created_at>
          <updated_at type="datetime">2013-08-02T18:04:45Z</updated_at>
          <email>ellend@mistborn.com</email>
          <data>Don't test everything here, since find_payment_method tests it all.</data>
          <storage_state>cached</storage_state>
          <last_four_digits>4942</last_four_digits>
          <card_type>master</card_type>
          <first_name>Eland</first_name>
          <last_name>Venture</last_name>
          <month type="integer">1</month>
          <year type="integer">2019</year>
          <address1>3 Main</address1>
          <address2>Suite 7</address2>
          <city>Oakland</city>
          <state>NJ</state>
          <zip>33221</zip>
          <country>UK</country>
          <phone_number>43</phone_number>
          <full_name>Eland Venture</full_name>
          <payment_method_type>credit_card</payment_method_type>
          <errors>
          </errors>
          <verification_value></verification_value>
          <number>XXXX-XXXX-XXXX-4942</number>
        </payment_method>
      </transaction>
"""

if __name__ == '__main__':
    unittest.main()
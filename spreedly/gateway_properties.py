from model import Model


class GatewayProperties(Model):
    fields = (
        'gateway_type',
        'name',
        'supported_countries',
        'homepage',
    )

    @classmethod
    def list_from_xml(cls, xml_doc):
        for xml_gateway in xml_doc.xpath('.//gateways/gateway'):
            GatewayProperties(xml_gateway)

    def __init__(self):
        self.supported_countries = []
        self.payment_methods = []

        super(GatewayProperties, self).__init__()
        self._init_supported_countries(xmldoc)
        self._init_payment_methods(xmldoc)

    def _init_supported_countries(self, xmldoc):
        countries = xmldoc.xpath('.//supported_countries').text
        self.supported_countries = countries.split(',')

    def _init_payment_methods(self, xmldoc):
        for xml_payment_method in xmldoc.xpath('.//payment_methods/payment_method').text:
            self.payment_methods.append(xml_payment_method[0].text)



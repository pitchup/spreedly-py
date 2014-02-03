from model import Model
from spreedly.common.fields import Field


class Gateway(Model):
    gateway_type = Field()
    state = Field()
    name = Field()

    def __init__(self, xml_doc):
        super(Gateway, self).__init__(xml_doc)
        self.credentials = {}
        self._init_credentials(xml_doc)

    @classmethod
    def list_from_xml(cls, xml_doc):
        gateways = []

        for xml_gateway in xml_doc.xpath('.//gateways/gateway'):
            gateways.append(Gateway(xml_gateway))

    def _init_credentials(self, xml_doc):
        for xml_credential in xml_doc.xpath('.//credentials/credential'):
            self.credentials[xml_credential.xpath('.//name')[0].text] = xml_credential.xpath('.//value')[0].text


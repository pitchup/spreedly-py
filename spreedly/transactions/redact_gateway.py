from spreedly.gateway import Gateway
from transaction import Transaction


class RedactGateway(Transaction):
    def __init__(self, xml_doc):
        super(RedactGateway, self).__init__(xml_doc)
        self.gateway = Gateway(xml_doc.find('.//gateway'))

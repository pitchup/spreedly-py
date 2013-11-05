import spreedly.common.error_parser as ep

class XmlErrorList(Exception):
    def __init__(self, xml_doc):
        ep.errors_from()


class AuthenticationError(XmlErrorList):
    pass


class NotFoundError(XmlErrorList):
    pass


class TransactionCreationError(XmlErrorList):
    pass


class PaymentRequiredError(XmlErrorList):
    pass


class TimeoutError(Exception):
    pass

class UnexpectedResponseError(Exception):
    pass


from connection import Connection
from lxml import etree
from error import *


def ssl_get(end_point, headers):
    return _ssl_request('get', end_point, headers)


def ssl_post(end_point, body, headers, talking_to_gateway=False):
    return _ssl_request('post', end_point, body, headers, {"talking_to_gateway": talking_to_gateway})


def ssl_raw_get(end_point, headers):
    return _ssl_request('get', end_point, None, headers, {'return_raw': True})


def ssl_put(end_point, body, headers):
    return _ssl_request('put', end_point, body, headers)


def ssl_options(end_point):
    return _ssl_request('options', end_point, None, {})


def _ssl_request(method, endpoint, body, headers, options=None):
    options = options or {}
    options.update({'taking_to_gateway': False, 'return_raw': False})

    response = raw_ssl_request(method, endpoint, etree.tostring(body), headers)
    show_raw_response(response.status_code, response.text)

    return handle_response(response, options['return_raw'])

    #TODO Handle timeout / connection errors.


def raw_ssl_request(method, endpoint, body, headers=None):
    connection = Connection(endpoint)
    return connection.request(method, body, headers)


def handle_response(response, return_raw):
    if 200 <= response.status_code <= 300:
        return response.text if return_raw else xml_doc(response)
    elif response.status_code == 401:
        raise AuthenticationError(xml_doc(response))
    elif response.status_code == 404:
        raise NotFoundError
    elif response.status_code == 402:
        raise PaymentRequiredError(xml_doc(response))
    elif response.status_code == 422:
        if xml_doc(response).xpath('.//errors/error'):
            raise TransactionCreationError(xml_doc(response))
        else:
            return xml_doc(response)


def show_raw_response(response_code, response_text):
    print "Response code: %s\nResponse body:\n%s" % (response_code, response_text)


def xml_doc(response):
    return etree.fromstring(response.text)
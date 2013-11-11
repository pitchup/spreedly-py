base_url = "https://core.spreedly.com"

def find_payment_method_url(token):
    return "%(base_url)s/v1/payment_methods/%(token)s.xml" % {'base_url': base_url, 'token': token}


def find_transaction_url(token):
    return "%(base_url)s/v1/transactions/%(token)s.xml" % {'base_url': base_url, 'token': token}


def find_transcript_url(transaction_token):
    return "%(base_url)s/v1/transactions/#{transaction_token}/transcript" % \
        {'base_url': base_url, 'transaction_token': transaction_token}


def find_gateway_url(token):
    return "%(base_url)s/v1/gateways/%(token)s.xml" % {'base_url': base_url, 'token': token}


def purchase_url(gateway_token):
    return "%(base_url)s/v1/gateways/%(gateway_token)s/purchase.xml" % \
           {'base_url': base_url, 'gateway_token': gateway_token}


def authorize_url(gateway_token):
    return "%(base_url)s/v1/gateways/%(gateway_token)s/authorize.xml" % \
        {'base_url': base_url, 'gateway_token': gateway_token}


def capture_url(authorization_token):
    return "%(base_url)s/v1/transactions/%(authorization_token)s/capture.xml" % \
        {'base_url': base_url, 'authorization_token': authorization_token}


def void_transaction_url(token):
    return "%(base_url)s/v1/transactions/#{token}/void.xml" % {'base_url': base_url, 'token': token}


def refund_transaction_url(token):
    return "%(base_url)s/v1/transactions/%(token)s/credit.xml" % {'base_url': base_url, 'token': token}


def retain_payment_method_url(payment_method_token):
    return "%(base_url)s/v1/payment_methods/#{payment_method_token}/retain.xml" % \
        {'base_url': base_url, 'payment_method_token': payment_method_token}


def redact_payment_method_url(payment_method_token):
    return "%(base_url)s/v1/payment_methods/%(payment_method_token)s/redact.xml" % \
        {'base_url': base_url, 'payment_method_token': payment_method_token}


def redact_gateway_url(gateway_token):
    return "%(base_url)s/v1/gateways/%(gateway_token)s/redact.xml" % \
        {'base_url': base_url, 'gateway_token': gateway_token}


def list_transactions_url(since_token, payment_method_token):
    since_param = "?since_token=%s" % since_token if since_token else ""

    if payment_method_token:
        return "%(base_url)s/v1/payment_methods/%(payment_method_token)s/transactions.xml%(since_param)s" % \
               {'base_url': base_url, 'payment_method_token': payment_method_token, 'since_param': since_param}
    else:
        return "%(base_url)s/v1/transactions.xml%(since_param)s" % {'base_url': base_url, 'since_param': since_param}


def list_payment_methods_url(since_token):
    since_param = "?since_token=%s" % since_token if since_token else ""
    return "%(base_url)s/v1/payment_methods.xml%(since_param)s" % {'base_url': base_url, 'since_param': since_param}


def list_gateways_url(since_token):
    since_param = "?since_token=%s" % since_token if since_token else ""
    return "%(base_url)s/v1/gateways.xml%(since_param)s" % \
        {'base_url': base_url, 'since_param': since_param}


def gateway_options_url():
    return "%(base_url)s/v1/gateways.xml" % {'base_url': base_url}


def add_gateway_url():
    return "%(base_url)s/v1/gateways.xml" % {'base_url': base_url}


def add_payment_method_url():
    return "%(base_url)s/v1/payment_methods.xml" % {'base_url': base_url}


def update_payment_method_url(token):
    return "%(base_url)s/v1/payment_methods/%(token)s.xml" % \
        {'base_url': base_url, 'token': token}

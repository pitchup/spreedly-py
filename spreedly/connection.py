import requests


class Connection(object):
    def __init__(self, endpoint):
        #TODO Might need to parse this..
        self.endpoint = endpoint

    def request(self, method, body, headers=None):
        #TODO Actual request here.
        requests_timeout = 64

        if method == "get":
            request = requests.get(self.endpoint, headers=headers, timeout=requests_timeout)
        elif method == "post":
            request = requests.post(self.endpoint, headers=headers, data=body, timeout=requests_timeout)
        elif method == "put":
            request = requests.put(self.endpoint, headers=headers, data=body, timeout=requests_timeout)
        elif method == "delete":
            request = requests.delete(self.endpoint, headers=headers, data=body, timeout=requests_timeout)
        elif method == "options":
            request = requests.options(self.endpoint, headers=headers, timeout=requests_timeout)
        else:
            raise RuntimeError("Unsupported request method %s", method)

        return request
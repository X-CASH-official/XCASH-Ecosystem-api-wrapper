import binascii

import json
import os
import requests


class XcashException(Exception):
    """Xcash Exceptions
    """
    pass


class InvalidArgument(XcashException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    pass


class MissingRequiredParameter(XcashException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        pass


class ParamNotSupported(XcashException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        pass


class AmountTypeError(XcashException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        pass


class AddressTypeError(XcashException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        pass


class MissingRequiredParama(XcashException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
        pass


class Helpers():
    def __init__(self):
        pass

    @staticmethod
    def check_url(delegate_url):
        """Check the delegate url

        Args:
            delegate_url (str): Provided url when initiating a class

        Returns:
            str: url
        """
        if not delegate_url[-1] == "/":
            return f'{delegate_url}/'
        else:
            return delegate_url

    def get_amount(self, atomic: int) -> float:
        """Convert atomic units to human readable format. 

        Args:
            atomic (int): amount of XCASH express atomic units

        Returns:
            int: Human readable verzion of XCASH amount
        """
        return atomic / (10 ** 6)

    def get_atomic(self, xcash_amount) -> int:
        """Convert XCASH to atomic value

        Args:
            xcash_amount (float, int): Xcash amount

        Returns:
            int: xcash amount in atomic reprezentation
        """

        return int(xcash_amount * (10 ** 6))

    def process_response(self, response):
        try:
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(err)
        except requests.exceptions.ConnectionError as err:
            raise Exception(err)

    def get_response(self, url):
        response = requests.get(url=url, headers={'Accept': 'application/json',
                                                  "Content-Type": "application/json"})

        return response

    def post_response(self, rpc_url, rpc_input, headers):
        return requests.post(rpc_url, data=json.dumps(rpc_input), headers=headers)

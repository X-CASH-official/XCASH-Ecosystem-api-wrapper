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
        """Process response

        Args:
            response (dict): response from the API call

        Raises:
            Exception: HTTP error
            Exception: Connection Error

        Returns:
            dict: Data from the api call
        """
        try:
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            raise Exception(err)
        except requests.exceptions.ConnectionError as err:
            raise Exception(err)

    def get_response(self, url: str):
        """Get response from GET request

        Args:
            url (str): string url 

        Returns:
            dict: Response from api call
        """
        response = requests.get(url=url, headers={'Accept': 'application/json',
                                                  "Content-Type": "application/json"})

        return response

    def post_response(self, rpc_url, rpc_input, headers):
        return requests.post(rpc_url, data=json.dumps(rpc_input), headers=headers)

    def get_payment_id(self) -> str:
        """Create payment ID for wallet

        Returns:
            str: random payment id
        """

        random_32_bytes = os.urandom(32)
        payment_id = "".join(map(chr, binascii.hexlify(random_32_bytes)))
        return payment_id

    def check_function_params(self, allowed_keys, kwargs):
        for k, v in kwargs.items():
            if k not in allowed_keys:
                raise InvalidArgument(f"Argument {k}  with value {v} is not supported in this API call")

    def check_params(self, allowed_keys, params):
        """Check the allowed elements

        Args:
            list_to_check (_type_): _description_
            params (dict): Params through kwargs

        Raises:
            MissingRequiredParameter: When required param is missing
        """

        for k in params.keys():
            if k not in allowed_keys:
                allowed = ', '.join(allowed_keys)
                raise ParamNotSupported(f'Parameter {k} not allowed. Available are: {allowed}')

    def process_destinations(self, destinations: list) -> list:
        """Helper function to process the transfer structure

        Args:
            destinations (list): List of destinations where funds will be sent

        Raises:
            AmountTypeError: If amount is in forms of string
            Exception: _description_
            MissingRequiredParama: If required params for destination are missing

        Returns:
            list: List of ready to send destinations formatted for RPC.
        """
        allowed = ("address", "amount")

        new_transfers = list()
        for d in destinations:
            formated_destination = dict(((k.lower(), v) for k, v in d.items()))
            if all(key in formated_destination for key in allowed):
                if not isinstance(formated_destination.get("amount"), (int, float)):
                    raise AmountTypeError("Amount needs to be either integer or float.")
                else:
                    formated_destination["amount"] = self.get_atomic(formated_destination.get("amount"))
                if not isinstance(formated_destination.get("address"), str):
                    raise AddressTypeError("Destination address is required to be string.")

                new_transfers.append(formated_destination)
            else:
                required = ' & '.join(allowed)
                raise MissingRequiredParama(f"One of the required params is missing. Required are {required}")
        return new_transfers

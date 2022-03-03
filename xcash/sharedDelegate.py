import requests
from xcash.helpers import Helpers


class SharedDelegate(Helpers):
    def __init__(self, delegate_url: str):
        Helpers.__init__(self)
        try:
            url = self.check_url(delegate_url=delegate_url)
            requests.get(url)
            self.delegate_api = url
        except requests.ConnectionError:
            raise ConnectionError
        except requests.exceptions.MissingSchema:
            raise requests.exceptions.MissingSchema

        self.delegate_website_statistics = "shareddelegateswebsitegetstatistics"
        self.delegate_found_blocks = "getblocksfound"
        self.public_address_info = "getpublicaddressinformation"
        self.public_address_payment_info = "getpublicaddresspaymentinformation"
        self.delegate_voter_list = "getdelegatesvoterslist"

    def get_blocks_found(self, start: int = 1, amount="all") -> list:
        """Get blocks found by the shared delegate

        Args:
            start (int, optional): Start of the block query. Defaults to 1.
            amount (str, int, optional): Number of blocks to return. Defaults to "all".

        Returns:
            list: list of blocks with details
        """

        response = self.get_response(
            url=self.delegate_api + f"{self.delegate_found_blocks}?start={start}&amount={amount}")
        return self.process_response(response)

    def get_delegate_voter_list(self, wallet_address: str = None) -> list:
        """Get a list of all delegates staking towards the shared delegate.

        Args:
            wallet_address (str, optional): The public address of the shared delegate. Defaults to None.

        Returns:
            list: Delegates staking to shared delegate
        """
        if not wallet_address:
            wallet_address = self.get_delegate_website_statistic()["public_address"]
        response = self.get_response(
            url=self.delegate_api + f"{self.delegate_voter_list}?parameter1={wallet_address}")
        return self.process_response(response)

    def get_delegate_website_statistic(self) -> dict:
        """Get statistics about the shared delegate

        Returns:
            dict: Statistical details and characteristics of shared delegate
        """

        response = self.get_response(url=self.delegate_api + self.delegate_website_statistics)
        return self.process_response(response)

    def get_public_address_information(self, public_address: str) -> dict:
        """	Get statistics about any delegate that has staked on the shared delegate

        Args:
            public_address (str): The public address of the delegate

        Returns:
            dict: statistics for the chosen delegate
        """

        response = self.get_response(
            url=self.delegate_api + f"{self.public_address_info}?public_address={public_address}")
        return self.process_response(response)

    def get_public_address_payment_information(self, public_address: str, start: int = 1, amount="all") -> list:
        """Get payment information about any delegate that has staked on the shared delegate

        Args:
            public_address (str): Delegates public address from where stake is sent
            start (int, optional): The start payment in the list. Defaults to 1.
            amount (str,int, optional): Amount of payments to return from start param. Defaults to "all".

        Returns:
            list: Payments sent to delegate
        """


        response = self.get_response(
            url=self.delegate_api + f"{self.public_address_payment_info}?public_address={public_address}&start={start}&amount={amount}")
        return self.process_response(response)


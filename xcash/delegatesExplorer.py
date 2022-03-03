from xcash.helpers import Helpers
from pprint import pprint


class DelegatesExplorer(Helpers):
    def __init__(self):
        super().__init__()
        self.base_url = "http://delegates.xcash.foundation/"
        self.delegates_website_get_statistics = "delegateswebsitegetstatistics"
        self.get_delegates = "getdelegates"
        self.delegate_stats = "getdelegatesstatistics"
        self.delegate_info = "getdelegatesinformation"
        self.delegate_voter_list = "getdelegatesvoterslist"
        self.round_statistics = "getroundstatistics"
        self.delegate_information = "getdelegatesinformation"
        self.param1 = "?parameter1="

    def get_delegate_website_statistics(self)-> dict:
        """Get overall statistics on the XCASH Dpops.

        Returns:
            dict: general statistics of the DPOPS system
        """
        response = self.get_response(url=self.base_url + self.delegates_website_get_statistics)
        return self.process_response(response)

    def get_all_delegates(self) -> list :
        """Get all delegates registered to XCASH DPops system

        Returns:
            list: list of delegates
        """
        response = self.get_response(url=self.base_url + self.get_delegates)
        return self.process_response(response)

    def get_delegate_statistics(self, delegate: str) -> dict:
        """Get general statistics of the delegate

        Args:
            delegate (str): delegate name or address

        Returns:
            dict: delegate general statistics
        """
        response = self.get_response(url=self.base_url + self.delegate_stats + self.param1 + f'{delegate}')
        return self.process_response(response)

    def get_delegate_information(self, delegate: str) -> dict:
        """Get delegate information 

        Args:
            delegate (str): delegate name or address

        Returns:
            dict: delegate information
        """
        response = self.get_response(url=self.base_url + self.delegate_info + self.param1 + f'{delegate}')
        return self.process_response(response)

    def get_delegate_voter_list(self, delegate: str) -> list:
        """Get list of voters for delegate

        Args:
            delegate (str): delegate name or address

        Returns:
            list: list of voters
        """
        response = self.get_response(url=self.base_url + self.delegate_voter_list + self.param1 + f'{delegate}')
        return self.process_response(response)

    def get_round_statistics(self, block_height: int)-> dict:
        """Get round statistics 

        Args:
            block_height (int): Block height number

        Returns:
            dict: The complete block that contains all of the reserve bytes
        """
        response = self.get_response(url=self.base_url + self.round_statistics + self.param1 + f'{block_height}')
        return self.process_response(response)


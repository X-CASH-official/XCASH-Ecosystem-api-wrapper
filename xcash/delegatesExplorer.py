from xcash.helpers import get_response, process_response
class DelegatesExplorer:
    def __init__(self, base_url: str = "http://delegates.xcash.foundation/"):
        self.base_url = base_url
        self.delegates_website_get_statistics = "delegateswebsitegetstatistics"
        self.get_delegates = "getdelegates"
        self.delegate_stats = "getdelegatesstatistics"
        self.delegate_info = "getdelegatesinformation"
        self.delegate_voter_list = "getdelegatesvoterslist"
        self.round_statistics = "getroundstatistics"
        self.delegate_information = "getdelegatesinformation"
        self.param1 = "?parameter1="

    def get_delegate_website_statistics(self) -> dict:
        """Get overall statistics on the XCASH Dpops.

        Returns:
            dict: general statistics of the DPOPS system
        """
        response = get_response(url=self.base_url + self.delegates_website_get_statistics)
        return process_response(response)

    def get_all_delegates(self) -> list:
        """Get all delegates registered to XCASH DPops system

        Returns:
            list: list of delegates
        """
        response = get_response(url=self.base_url + self.get_delegates)
        return process_response(response)

    def get_delegate_statistics(self, delegate: str) -> dict:
        """Get general statistics of the delegate

        Args:
            delegate (str): delegate name or address

        Returns:
            dict: delegate general statistics
        """
        response = get_response(url=self.base_url + self.delegate_stats + self.param1 + f'{delegate}')
        return process_response(response)

    def get_delegate_information(self, delegate: str) -> dict:
        """Get delegate information 

        Args:
            delegate (str): delegate name or address

        Returns:
            dict: delegate information
        """
        response = get_response(url=self.base_url + self.delegate_info + self.param1 + f'{delegate}')
        return process_response(response)

    def get_delegate_voter_list(self, delegate: str) -> list:
        """Get list of voters for delegate

        Args:
            delegate (str): delegate name or address

        Returns:
            list: list of voters
        """
        response = get_response(url=self.base_url + self.delegate_voter_list + self.param1 + f'{delegate}')
        return process_response(response)

    def get_round_statistics(self, block_height: int) -> dict:
        """Get round statistics 

        Args:
            block_height (int): Block height number

        Returns:
            dict: The complete block that contains all of the reserve bytes
        """
        response = get_response(url=self.base_url + self.round_statistics + self.param1 + f'{block_height}')
        return process_response(response)

    # Setters
    def set_base_url(self, base_url: str) -> None:
        """Set base url 

        Args:
            base_url (str): New base url
        """
        self.base_url = base_url

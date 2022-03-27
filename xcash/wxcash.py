import requests
import json
from pprint import pprint
from xcash.helpers import Helpers


class wXcash(Helpers):
    def __init__(self, api_key: str):
        super().__init__()
        self.api = "https://api.polygonscan.com/api?"
        self.wxcash_contract = "0x235328f864f38a91f0d2282159ea7c7b7c9f7c62"
        self.foundation_wallet = "0x03678f2c2c762DC63c2Bb738c3a837D366eDa560"
        self.api_key = f'&apikey={api_key}'

        self.address = "&address="
        self.contract_address = '&contractaddress='

        ## Modules
        self.stats = "module=stats"
        self.account = "module=account"
        self.token = "module=token"

        ## action
        self.token_supply = "&action=tokensupply"
        self.token_balance = "&action=tokenbalance"
        self.token_supply_hist = "&action=tokensupplyhistory"

        # Other
        self.tag_latest = f'&tag=latest'
        self.block_number = f'&blockno= '

    @staticmethod
    def result_conversion(result):
        """
        This method has to be isued to convert the string into list
        """
        return json.loads(result)

    def supply(self) -> dict:
        """
        Returns the total supply of the WXCASH. Supply express on 18 decimals
        """
        self.url = self.api + self.stats + self.token_supply + self.foundation_wallet + self.api_key
        response = self.get_response(self.url)
        return self.process_response(response)

    def hist_supply(self, block_height: int):
        """
        Get historical supply of WXCASh based on block height
        """
        self.url = self.api + self.stats + self.token_supply_hist + self.contract_address + self.wxcash_contract + self.block_number + str(
            block_height) + self.api_key
        response = self.get_response(self.url)
        return self.process_response(response)

    def info(self):
        self.url = self.api + self.token + self.contract_address + self.wxcash_contract + self.api_key
        response = self.get_response(self.url)
        return self.process_response(response)

    # https://docs.polygonscan.com/api-endpoints/tokens



if __name__ == "__main__":
    wxcsah = wXcash(api_key="67F34NNBNR5PFSNW6FVTY7TNG8TF9MV9BH")
    supply = wxcsah.info()
    pprint(supply)

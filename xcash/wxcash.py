import requests
import json
from pprint import pprint
from xcash.helpers import Helpers


class wXcash(Helpers):
    def __init__(self, api_key: str):
        super().__init__()
        self.api = "https://api.polygonscan.com/api?"
        self.wxcash_contract = "&contractaddress=0x235328f864f38a91f0d2282159ea7c7b7c9f7c62"
        self.foundation_wallet = "&contractaddress=0x03678f2c2c762DC63c2Bb738c3a837D366eDa560"
        self.api_key = f'&apikey={api_key}'

        ## Modules
        self.stats = "module=stats"

        ## action
        self.token_supply = "&action=tokensupply"

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


if __name__ == "__main__":
    wxcsah = wXcash(api_key="67F34NNBNR5PFSNW6FVTY7TNG8TF9MV9BH")
    supply = wxcsah.supply()
    pprint(supply)

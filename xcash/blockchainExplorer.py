from .helpers import get_response, process_response


class BlockchainExplorer:
    def __init__(self, base_api: str = "https://explorer.xcash.foundation/"):
        """
        Delegate constructor

        :delegate_url: Address of the delegate
        """

        self.base_api = base_api
        self.generates_supply = "getgeneratedsupply"
        self.circulating_supply = "getcirculatingsupply"
        self.blockchain_data = "getblockchaindata"
        self.block_height = "getcurrentblockheight"
        self.last_block_data = "getlastblockdata"
        self.transaction_data = "gettransactiondata"
        self.transaction_confirmation = "gettransactionconfirmations"
        self.verify_reserve_proof = "verifyreserveproofapi"
        self.integrated_address = "createintegratedaddressapi"
        self.hash_data = "?tx_hash="
        self.block_data = "?block_data="
        self.public_address = "?public_address="
        self.reserve_proof = "&reserve_proof="
        self.data = "&data="
        self.payment_id = "&payment_id="

    def get_blockchain_data(self) -> dict:
        """Get overall and latest blockchain data

        Returns:
            dict: blockchain data
        """
        response = get_response(url=self.base_api + self.blockchain_data)
        return process_response(response)

    def get_circulating_supply(self) -> int:
        """Get current XCASH circulating supply

        Returns:
            int: circulating supply amount
        """
        response = get_response(url=self.base_api + self.circulating_supply)
        return process_response(response)

    def get_current_block_height(self) -> dict:
        """Get current block height of the XCASH chain 

        Returns:
            dict: block height count/number
        """
        response = get_response(url=self.base_api + self.block_height)
        return process_response(response)

    def get_generated_supply(self) -> int:
        """Get generated supply

        Returns:
            int: Total generated supply amount
        """
        response = get_response(url=self.base_api + self.generates_supply)
        return process_response(response)

    def get_last_block_data(self) -> dict:
        """Get last block details

        Returns:
            dict: details on the last block
        """
        response = get_response(url=self.base_api + self.last_block_data)
        return process_response(response)

    def get_block_data(self, block_data) -> dict:
        """Get block data based on provided argument.

        Args:
            block_data (str, int): Block hash or block height

        Returns:
            dict: block details 
        """
        response = get_response(url=self.base_api + self.last_block_data + self.block_data + f'{block_data}')
        return process_response(response)

    def get_transaction_data(self, tx_hash: str) -> dict:
        """Get the transaction data based on specified transaction hash

        Args:
            tx_hash (str): String of transaction hash

        Returns:
            dict: data on transaction
        """

        response = get_response(url=self.base_api + self.transaction_data + self.hash_data + f'{tx_hash}')
        return process_response(response)

    def get_reserve_proof_verification(self, public_address: str, reserve_proof: str, data: str = None) -> dict:
        """Verify reserver proof based on provided arguments

        Args:
            public_address (str): Valid public addres from XCASH 
            reserve_proof (str): Reserve proof
            data (str, optional): Any data that was used to create the reserve proof. Defaults to None.

        Returns:
            dict: Three different types of results in regards to reserve proof verification
        """
        response = get_response(
            url=self.base_api + self.verify_reserve_proof + self.public_address + f'{public_address}' + self.reserve_proof + f"{reserve_proof}" + self.data + f"{data}")
        return process_response(response)

    def generate_integrated_address(self, public_address: str, payment_id: str = None) -> dict:
        """Create integrated address for public address.

        Args:
            public_address (str): Valid public addres from XCASH 
            payment_id (str, optional): Payment ID if desired otherwise automatically created. Defaults to None.

        Returns:
            dict: details on integrated address
        """
        response = get_response(
            url=self.base_api + self.integrated_address + self.public_address + f'{public_address}' + self.payment_id + f'{payment_id}')
        return process_response(response)

    # Setters 
    def set_base_api(self, base_api: str) -> None:
        """Set base api 

        Args:
            base_api (str): New base api
        """
        self.base_api = base_api

import requests
import json
from xcash.helpers import Helpers


class XcashDaemonRpc(Helpers):
    def __init__(self, rpc_url: str = None):
        """XCASH Daemon RPC Class

        Args:
            rpc_url (str, optional): daemon address. Defaults to http://localhost:18281/json_rpc.
        """

        super().__init__()
        self.headers = {'Content-Type': 'application/json'}

        if rpc_url:
            self.rpc_url = rpc_url

        else:
            self.rpc_url = "http://localhost:18281/json_rpc"

    def __xcash_daemon_post(self, method: str, params: (dict, list) = None) -> dict:
        """Post to XCASH Daemon RPC

        Args:
            method (str): Supported method by XCASH Daemon RPC
            params (dict, optional): Additional params to be sent through. Defaults to None.

        Returns:
            dict: result from api call
        """
        if not params:
            rpc_data = json.dumps({"jsonrpc": "2.0", "id": "0",
                                   "method": method, "params": params})

        else:
            rpc_data = json.dumps({"jsonrpc": "2.0", "id": "0",
                                   "method": method})

        response = requests.post(self.rpc_url, data=rpc_data, headers=self.headers)
        return self.process_response(response=response)

    def get_block_count(self) -> dict:
        """Look up how many blocks are in the longest chain known to the node. 

        Returns:
            dict: count - number of blocks in the longest chain, status - General RPC error
        """
        data = self.__xcash_daemon_post(method="get_block_count")
        return data

    def on_get_block_hash(self, block_height: int) -> dict:
        """Look up a block's hash by its height.Block header information can be 
            retrieved using either a block's hash or height. This method includes a 
            block's hash as an input parameter to retrieve basic inform

        Args:
            block_height (int): int array of length 1

        Returns:
            dict: block hash string
        """
        data = self.__xcash_daemon_post(method="on_get_block_hash", params=[block_height])
        return data

    def get_block_template(self, wallet_address: str, reserve_size: int) -> dict:
        """Get a block template on which mining a new block.

        Args:
            wallet_address (str): Address of wallet to receive coinbase transactions if block is mined
            reserve_size (int): Reserve Size

        Returns:
            dict: _description_
        """
        params = {"wallet_address": wallet_address, "reserve_size": reserve_size}
        data = self.__xcash_daemon_post(method="get_block_template", params=params)
        return data

    def submit_block(self, block_blob_data: list) -> dict:
        """Submit a mined block to network

        Args:
            block_blob_data (list): Array list of block blobs which have been mined. 
                                    See get_block_template to get a blob on which to mine.

        Returns:
            dict: block submit status
        """

        data = self.__xcash_daemon_post(method="submit_block", params=block_blob_data)
        return data

    def get_last_block_header(self) -> dict:
        """Block header information for the most recent block is easily
            retrieved with this method. No inputs are needed.

        Returns:
            dict: Structure containing block header
        """

        data = self.__xcash_daemon_post(method="get_last_block_header")
        return data

    def get_block_header_by_hash(self, hash: str) -> dict:
        """Block header information can be retrieved using either a block's hash 
        or height. This method includes a block's hash as an input parameter to 
        retrieve basic information about the block.

        Args:
            hash (str): The block's sha256 hash.

        Returns:
            dict: block_header, status and boolean of untrusted
        """
        params = {"hash": hash}

        data = self.__xcash_daemon_post(method="get_block_header_by_hash", params=params)
        return data

    def get_block_header_by_height(self, height: int) -> dict:
        """Similar to get_block_header_by_hash above, this method includes a block's height 
        as an input parameter to retrieve basic information about the block.

        Args:
            height (str): he block's height.

        Returns:
            dict: block_header, status and boolean of untrusted
        """
        params = {"height": height}

        data = self.__xcash_daemon_post(method="get_block_header_by_height", params=params)
        return data

    def get_block_headers_range(self, start_height: int, end_height: int) -> dict:
        """Similar to get_block_header_by_height above, but for a range of blocks. 
        This method includes a starting block height and an ending block height as parameters 
        to retrieve basic information about the range of blocks.

        Args:
            start_height (int): The starting blocks height
            end_height (int): The ending block's height

        Returns:
            dict: _description_
        """
        params = {"start_height": start_height, "end_height": end_height}
        data = self.__xcash_daemon_post(method="get_block_headers_range", params=params)
        return data

    def get_block(self, height_hash) -> dict:
        """Similar to get_block_header_by_height above, but for a range of blocks. 
        This method includes a starting block height and an ending block height as parameters 
        to retrieve basic information about the range of blocks.

        Args:
            height_hash (int,str): Integer for the query by height, str for query by hash

        Returns:
            dict: _description_
        """

        if isinstance(height_hash, int):
            params = {"height": height_hash}
        elif isinstance(height_hash, str):
            params = {"hash": height_hash}
        else:
            raise Exception("Integer for the query by height, str for query by hash")

        return self.__xcash_daemon_post("get_block", params)

    def get_connections(self) -> dict:
        """Retrieve information about incoming and outgoing connections to your node.

        Returns:
            list: list of all connections an their info
        """

        return self.__xcash_daemon_post(method="get_connections")

    def get_info(self) -> dict:
        """Retrieve general information about the state of your node and the network.

        Returns:
            dict: information 
        """

        return self.__xcash_daemon_post(method="get_info")

    def hard_fork_info(self) -> dict:
        """Look up information regarding hard for voting and readiness

        Returns:
            dict: Data on hardfork
        """

        return self.__xcash_daemon_post(method="hard_fork_info")

    def set_bans(self, nodes_to_ban: list) -> dict:
        pass

    def get_bans(self) -> dict:
        """Get list of banned IPs

        Returns:
            dict: list of banned IPs
        """
        return self.__xcash_daemon_post(method="get_bans")

    def flush_txpool(self) -> dict:

        return self.__xcash_daemon_post(method="flush_txpool")

    def get_output_histogram(self, amounts: list) -> dict:
        """Get a histogram of output amounts. For all amounts (possibly filtered by parameters), 
        gives the number  of outputs on the chain for that amount. RingCT outputs counts as 0 amount.

        Args:
            amounts (list): list of unsigned ints

        Returns:
            dict: histogram of entries
        """
        params = {"amounts": amounts}
        return self.__xcash_daemon_post(method="get_output_histogram", params=params)

    def get_coinbase_tx_sum(self, height: int, count: int) -> dict:
        """Get the coinbase amount and the fees amount for n last blocks starting 
        at particular height

        Args:
            height (int): Block height from which getting the amounts
            count (int):  number of blocks to include in the sum

        Returns:
            dict: _description_
        """
        params = {"height": height, "count": count}
        return self.__xcash_daemon_post(method="get_coinbase_tx_sum", params=params)

    def get_version(self) -> dict:
        """Current deployed version

        Returns:
            dict: status and version 
        """

        return self.__xcash_daemon_post(method="get_version")

    def get_fee_estimate(self) -> dict:
        """Gives an estimation on fees per kB.
        Returns:
            dict: status and version 
        """

        return self.__xcash_daemon_post(method="get_fee_estimate")

    def get_alternate_chains(self) -> dict:
        """Display alternative chains seen by the node.
        Returns:
            dict: array of chains, difficulty, height, length
        """

        return self.__xcash_daemon_post(method="get_alternate_chains")

    def relay_tx(self, tx_ids: list) -> dict:
        """Relay a list of transaction IDs.

        Args:
            tx_ids (list): List of transaction IDs to relay

        Returns:
            dict: status
        """

        return self.__xcash_daemon_post(method="relay_tx", params=tx_ids)

    def sync_info(self) -> dict:
        """Get synchronisation information

        Returns:
            dict: height, peers, spans, status, target_height
        """

        return self.__xcash_daemon_post(method="sync_info")

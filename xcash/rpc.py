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

    def __xcash_daemon_post(self, method: str, params = None) -> dict:
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


class XcashWalletRpc(Helpers):
    def __init__(self, wallet_rpc_url=None):
        """Xcash Wallet Rpc Class.

        Args:
            wallet_rpc_url (str, optional): Custom rpc url otherwise. Defaults to "http://localhost:18285/json_rpc".
        """
        super().__init__()
        self.headers = {'Content-Type': 'application/json'}

        if wallet_rpc_url:
            self.rpc_url = wallet_rpc_url
        else:
            self.rpc_url = "http://localhost:18285/json_rpc"

    def __xcash_wallet_post(self, method: str, params=None) -> dict:
        """Post to XCASH Wallet RPC

        Args:
            method (str): Supported method by XCASH Daemon RPC
            params (dict, optional): Additional params to be sent through. Defaults to None.

        Returns:
            dict: result from api call
        """
        if params:
            rpc_data = json.dumps({"jsonrpc": "2.0", "id": "0",
                                   "method": method, "params": params})

        else:
            rpc_data = json.dumps({"jsonrpc": "2.0", "id": "0",
                                   "method": method})

        response = requests.post(self.rpc_url, data=rpc_data, headers=self.headers)
        return self.process_response(response=response)

    def get_balance(self, account_index: int = 0, sub_address_indicies: list=None) -> dict:
        """Return the wallet's balance.‌

        Args:
            account_index (int, optional): Return balance for this account.. Defaults to 0.
            sub_address_indicies (list, optional): Return balance detail for those subaddresses. Defaults to None.

        Returns:
            dict: balance, unlocked_balance, multisig_import_needed, per_subaddress
        """
        params = {}
        if account_index:
            params.update({"account_index": account_index})

        if sub_address_indicies:
            params.update({"address_indices": sub_address_indicies})
        return self.__xcash_wallet_post(method="get_balance", params=params)

    def get_address(self, account_index: int, address_index: list = None) -> dict:
        """Return the wallet's addresses for an account. Optionally filter for specific set of subaddresses.‌

        Args:
            account_index (int): Return subaddresses for this account.
            address_index (list, optional): List of subaddresses to return from an account. Defaults to None.

        Returns:
            dict: _description_
        """
        params = {"account_index": account_index}
        if address_index:
            params.update({"address_index": address_index})

        return self.__xcash_wallet_post(method="get_address", params=params)

    def get_address_index(self, address: str) -> dict:
        """Get account and address indexes from a specific (sub)address‌

        Args:
            address (str): Valid Xcash address

        Returns:
            dict: index
        """
        params = {"address":"address"}
        return self.__xcash_wallet_post(method="get_address_index", params=params)

    def create_address(self, account_index: int, label: str = None) -> dict:
        """Create a new address for an account. Optionally, label the new address.‌

        Args:
            account_index (int): Create a new address for this account.
            label (str, optional): Label for the new address.. Defaults to None.

        Returns:
            dict: address, ddress_index
        """
        params = {"account_index": account_index}
        if label:
            params.update({"label": label})

        return self.__xcash_wallet_post(method="create_address", params=params)

    def label_address(self, major: int, minor: int, label: str) -> dict:
        """Label an address

        Args:
            major (int): Account index for the subaddress.
            minor (int): Index of the subaddress in the account.
            label (str):  Label for the address.

        Returns:
            dict: None
        """
        params = {"index": {"major": major, "minor": minor}, "label": label}

        return self.__xcash_wallet_post(method="label_address", params=params)

    def get_accounts(self, tag: str = None) -> dict:
        """Get all accounts for a wallet. Optionally filter accounts by tag.‌

        Args:
            tag (str, optional): Tag for filtering accounts.. Defaults to None.
        
        Returns:
            dict: subaddress_accounts, total_balance, total_unlocked_balance 
        """
        params = {}
        if tag:
            params.update({"tag": tag})

        return self.__xcash_wallet_post(method="get_accounts", params=params)

    def create_account(self, label: str = None) -> dict:
        """Create a new account with an optional label.‌

        Args:
            label (str, optional):  Label for the account.. Defaults to None.

        Returns:
            dict: account_index, address
        """
        params = {}
        if label:
            params.update({"label": label})
        return self.__xcash_wallet_post(method="create_account", params=params)

    def label_account(self, account_index: int, label: str) -> dict:
        """Label an account

        Args:
            account_index (int): Apply label to account at this index
            label (str): Label for the account

        Returns:
            dict: None
        """
        params = ({"account_index": account_index, "label": label})
        return self.__xcash_wallet_post(method="label_account", params=params)

    def get_account_tags(self) -> list:
        """Get a list of user defined account tags

        Returns:
            list: account_tags
        """
        return self.__xcash_wallet_post(method="get_account_tags")

    def tag_accounts(self, tag: str, accounts: list) -> dict:
        """Apply a filtering tag to a list of accounts

        Args:
            tag (str): Tag for the accounts
            accounts (list): Tag this list of accounts, array of unsigned integers.

        Returns:
            dict: None
        """
        params = {"tag": tag, "accounts": accounts}
        return self.__xcash_wallet_post(method="tag_accounts", params=params)

    def untag_accounts(self, accounts: list) -> dict:
        """Remove filtering tag from a list of accounts.‌

        Args:

            accounts (list): Remove tag from this list of accounts, array of insigned integers.

        Returns:
            dict: None
        """
        params = {"accounts": accounts}
        return self.__xcash_wallet_post(method="untag_accounts", params=params)

    def set_account_tag_description(self, tag: str, description: str) -> dict:
        """Set descritpion for an account tah

        Args:
            tag (str): Set a description for this tag
            description (str): description for the tag

        Returns:
            dict: None
        """
        params = {"tag": tag, "description": description}
        return self.__xcash_wallet_post(method="set_account_tag_description", params=params)

    def get_wallet_height(self) -> int:
        """Get the wallets current block height

        Returns:
            int: the current xcash-wallet-rpc's blockchain height. If the wallet has 
                been offline for a long time, it may need to catch up with the daemon.
        """
        return self.__xcash_wallet_post(method="get_height")

    def transfer(self, destinations: list, priority: int = 0, mixin: int = 20, **kwargs) -> dict:
        """Initiate transfer to provided destinations. Integrated helpers as well to check destination structure
            and allowed params according to the demands of the chain

        Args:
            destinations (list): List of destination as dictionary constructed with recipient {"address":"XCA...", "amount":100000}
            mixin (int, optional): Number of outputs from the blockchain to mix with . Defaults to 20.
            payment_id (str, optional): _description_. Defaults to None.
        Returns:
            dict: amount, fee, multisig_txset, tx_blobl, tx_hash, tx_key, tx_metadata, unsigned_txset
        """

        allowed_keys = ["account_index", "subaddr_indices", "get_tx_key", "ring_size", "payment_id", "do_not_relay",
                        "get_tx_metadata"]

        params = {"mixin": mixin,
                  "unlock_time": 0,
                  "priority": priority,
                  "get_tx_key": True}

        # Check kwargs if they are allowed
        if kwargs:
            self.check_params(allowed_keys=allowed_keys, params=kwargs)
            params.update(kwargs)

        # Process recipients
        recipients = self.process_destinations(
            destinations=destinations)  # Check the destination structures to be correct and format amount
        params["destinations"] = recipients

        return self.post_to_monero_wallet_rpc("transfer", params)

    def transfer_split(self, destinations: list, priority: int = 0, mixin: int = 20, **kwargs) -> dict:
        """Same as transfer, but can split into more than one tx if necessary.‌

        Args:
            destinations (list): List of destinations represented as dict per destination constructued from address and amount
            priority (int, optional): et a priority for the transactions. Accepted Values are: 0-3 for: default, unimportant, normal, elevated, priority.. Defaults to 0.
            mixin (int, optional): Number of outputs from the blockchain to mix with (0 means no mixing).. Defaults to 20.

        Returns:
            dict: _description_
        """
        allowed_keys = ["account_index", "subaddr_indices", "get_tx_key", "ring_size", "payment_id", "do_not_relay",
                        "get_tx_metadata", "new_algorithm"]

        params = {"mixin": mixin,
                  "unlock_time": 0,
                  "priority": priority,
                  "get_tx_key": True}

        # Check kwargs if they are allowed
        if kwargs:
            self.check_params(allowed_keys=allowed_keys, params=kwargs)
            params.update(kwargs)

        # Process recipients
        recipients = self.process_destinations(
            destinations=destinations)  # Check the destination structures to be correct and format amount
        params["destinations"] = recipients
        return self.__xcash_wallet_post(method="transfer_split", params = params)

    def sign_transfer(self, unsigned_txset:str, export_raw:bool= False) -> dict:
        """Sign a transaction created on a read-only wallet (in cold-signing process)‌

        Args:
            unsigned_txset (str): Set of unsigned tx returned by "transfer" or "transfer_split" methods.
            expor_raw (bool, optional): Return the raw transaction data.. Defaults to False.

        Returns:
            dict: signed_txset, tx-Hash_list, tx_raw_list
        """

        params = {"unsigned_txset ": unsigned_txset}
        if export_raw:
            params.update({"export_raw ": export_raw})
        return self.__xcash_wallet_post(method="sign_transfer", params=params)


    def submint_transfer(self, tx_data_hex:str) -> dict:
        """Submit a previously signed transaction on a read-only wallet (in cold-signing process).‌

        Args:
            tx_data_hex (str): Set of signed tx returned by "sign_transfer"

        Returns:
            dict: tx_hash_list
        """
        params = {"tx_data_hex ": tx_data_hex}

        return self.__xcash_wallet_post(method="submint_transfer", params=params)

    def sweep_dust(self, **kwargs) -> dict:
        """Send all dust outputs back to the wallet's, to make them easier to spend (and mix).‌

        Kwargs:
            get_tx_keys (bool): Return the transaction keys after sending.
            do_not_relay (bool): If true, the newly created transaction will not be relayed to the X-Cash network. (Defaults to false)
            get_tx_hex (bool): Return the transactions as hex string after sending. (Defaults to false)
            get_tx_metadata (bool): Return list of transaction metadata needed to relay the transfer later. (Defaults to false)

        Returns:
            dict: tx_hash_list, tx_key_list, amount_list, fee_list, tx_blob_list, tx_metadata_list, multisig_txset, unsigned_txset
        """
        allowed = ["get_tx_keys","do_not_relay", "get_tx_hex","get_tx_metadata"]
        self.check_params(allowed_keys=allowed, params=kwargs)
        return self.__xcash_wallet_post(method="submint_transfer", params=kwargs)

    def sweep_all(self, address:str, account_index:int = 0, mixin:int = 20, **kwargs) -> dict:
        """Send all unlocked balance to an address.‌

        Args:
            address (str): Valid X-CASH address
            account_index (int, optional): Sweep transactions from this account.Defaults to 0.
            mixin (int, optional): Number of outputs from the blockchain to mix with (0 means no mixing).. Defaults to 20.

        Returns:
            dict: tx_hash_list, tx_key_list, amount_list, fee_list, tx_blobl_list, tx_metadata_list, multisig_txset, unsigned_txset
        """
        
        allowed = ["subaddr_indices", "priority", "payment_id","ring_size", "get_tx_keys","below_amount","do_not_relay","get_tx_hex","get_tx_metadata"]       
        self.check_params(allowed_keys=allowed, params=kwargs)

        params = {"address":address,"account_index":account_index,"mixin":mixin}
        if kwargs:
            params.update(kwargs)
        return self.__xcash_wallet_post(method="sweep_all", params=kwargs)

    def sweep_single(self, destinations:list, account_index:int = 0,mixin:int = 20, **kwargs) -> dict:
        """Send all of a specific unlocked output to an address.‌

        Args:
            destinations (list): Destination public address.
            account_index (int, optional): Sweep transactions from this account.. Defaults to 0.
            mixin (int, optional): Number of outputs from the blockchain to mix with (0 means no mixing).. Defaults to 20.

        Returns:
            dict: tx_hash_list, tx_key_list, amount_list, fee_ist, tx_blobl_list, tx_metadata_list, multisig_txset, unsigned_txset
        """

        allowed = ["subaddr_indices", "priority", "payment_id","ring_size", "get_tx_keys","below_amount","do_not_relay","get_tx_hex","get_tx_metadata"]       
        self.check_params(allowed_keys=allowed, params=kwargs)
        destinations =  self.process_destinations(destinations=destinations)

        params = {"destinations":destinations,"mixin":mixin,"account_index":account_index}
        if kwargs:
            params.update(kwargs)
        return self.__xcash_wallet_post(method="sweep_single", params=kwargs)

    def relay_tx(self, hex: str) -> dict:
        """Relay a transaction previously created with "do_not_relay":true.‌

        Args:
            hex (str): transaction metadata returned from a
             transfer method with get_tx_metadata set to true.

        Returns:
            dict: tx_hash
        """
        params = {"hex": hex}
        return self.__xcash_wallet_post(method="relay_tx", params=params)

    def store(self):
        """Save the wallet file

        Returns:
            file: None
        """
        return self.__xcash_wallet_post(method="store")

    def get_payments(self, payment_id: str) -> dict:
        """Get a list of incoming payments using a given payment id.‌

        Args:
            payment_id (str, optional): Payment ID used to find the payments (16 characters hex).. Defaults to None.

        Returns:
            dict: payments
        """

        params = {}
        if payment_id:
            params.update({"payment_id": payment_id})

        return self.__xcash_wallet_post(method="get_payments", params=params)

    def get_bulk_payments(self, payment_ids: list, min_block_height: int) -> dict:
        """Get a list of incoming payments using a given payment id, or a list of 
        payments ids, from a given height. This method is the preferred method over
         get_paymentsbecause it has the same functionality but is more extendable.
          Either is fine for looking up transactions by a single payment ID.‌

        Args:
            payment_ids (list): Payment IDs used to find the payments (16 characters hex).
            min_block_height (int): The block height at which to start looking for payments.

        Returns:
            dict: List of payments
        """
        params = {"payment_ids": payment_ids, "min_block_height": min_block_height}
        return self.__xcash_wallet_post(method="get_payments", params=params)

    def incoming_transfers(self, transfer_type: str, account_index: int = 0, subaddrr_indices: list = None,
                           verbose: bool = True) -> dict:
        """Return a list of incoming transfers to the wallet

        Args:
            transfer_type (str):"all": all the transfers, 
                                "available": only transfers which are not yet spent 
                                "unavailable": only transfers which are already spent.
            account_index (int, optional): Return transfers for this account. Defaults to 0.
            subaddrr_indices (list, optional):  Return transfers sent to these subaddresses.. Defaults to None.
            verbose (bool, optional): Enable verbose output. Defaults to True.

        Returns:
            dict: list of transfers
        """
        params = {"transfer_type": transfer_type, "account_index": account_index, "subaddrr_indices": subaddrr_indices,
                  "verbose": verbose}
        return self.__xcash_wallet_post(method="incoming_transfers", params=params)

    def query_key(self, key_type: str) -> dict:
        """Return the spend or view private key.‌

        Args:
            key_type (str): Which key to retrieve: 
                            "mnemonic" - the mnemonic seed (older wallets do not have one)
                            "view_key" - the view key

        Returns:
            dict: key, a hex encoded, while the mnemonic will be a string of words.
        """
        params = {"key_type": key_type, }
        return self.__xcash_wallet_post(method="query_key", params=params)

    def make_integrated_address(self, standard_address: str = None, payment_id: str = None) -> dict:
        """Make an integrated address from the wallet address and a payment id.‌

        Args:
            standard_address (str, optional):  Destination public address.. Defaults to primary address.
            payment_id (str, optional): 16 characters hex encoded.. Defaults to random.

        Returns:
            dict: integrated_address, payment_id
        """
        params = {}
        if standard_address or payment_id:
            params.update({"standard_address": standard_address, "payment_id": payment_id})
        return self.__xcash_wallet_post(method="make_integrated_address", params=params)

    def split_integrated_address(self, integrated_address: str) -> dict:
        """Retrieve the standard address and payment id corresponding to an integrated address.‌

        Args:
            integrated_address (str): string

        Returns:
            dict: is_subaddress, payment, standard address
        """
        params = {"integrated_address": integrated_address, }
        return self.__xcash_wallet_post(method="split_integrated_address", params=params)

    def stop_wallet(self):
        """Stops the wallet, storing the curretn state

        Returns:
            None
        """
        return self.__xcash_wallet_post(method="stop_wallet")

    def rescan_blockchain(self):
        """Rescan the blockchain from scratch, losing any information which can 
        not be recovered from the blockchain itself. This includes destination addresses, 
        tx secret keys, tx notes, etc.‌
        """
        return self.__xcash_wallet_post(method="rescan_blockchain")

    def set_tx_notes(self, tx_ids: list, notes: list):
        """Set arbitrary string notes for transactions.‌

        Args:
            tx_ids (list): list of strings of transaction ids
            notes (list): notes for the transactions as list
        """
        params = {"txids": tx_ids, "notes": notes}
        return self.__xcash_wallet_post(method="set_tx_notes", params=params)

    def get_tx_notes(self, tx_ids: list) -> dict:
        """Get string notes for transactions.‌

        Args:
            tx_ids (list): transaction ids

        Returns:
            dict: notes
        """

        params = {"txids": tx_ids}
        return self.__xcash_wallet_post(method="get_tx_notes", params=params)

    def set_attribute(self, key: str, value: str) -> dict:
        """Set arbitrary attribute.‌

        Args:
            key (str): attribute name
            value (str):  attribute value

        Returns:
            dict: None
        """

        params = {"key": key, "value": value}
        return self.__xcash_wallet_post(method="set_attribute", params=params)

    def get_attribute(self, key: str) -> dict:
        """Set arbitrary attribute.‌

        Args:
            key (str): attribute name

        Returns:
            dict: value
        """

        params = {"key": key}
        return self.__xcash_wallet_post(method="get_attribute", params=params)

    def get_tx_key(self, tx_id: str) -> dict:
        """Get transaction secret key from transaction id.‌

        Args:
            tx_id (str): transaction id.

        Returns:
            dict: tx_key
        """

        params = {"txid": tx_id}
        return self.__xcash_wallet_post(method="get_tx_key", params=params)

    def check_tx_key(self, tx_id: str, tx_key: str, address: str) -> dict:
        """Check a transaction in the blockchain with its secret key.‌

        Args:
            tx_id (str):  transaction id.
            tx_key (str): transaction secret key.
            address (str): destination public address of the transaction.

        Returns:
            dict: confirmations, in_pool, received
        """
        params = {"txid": tx_id, "txkey": tx_key, "address": address}
        return self.__xcash_wallet_post(method="check_tx_key", params=params)

    def get_tx_proof(self, tx_id: str, address: str, message: str = None) -> dict:
        """Get transaction signature to prove it.‌

        Args:
            tx_id (str): transaction id.
            address (str):  destination public address of the transaction.
            message (str, optional): add a message to the signature to further 
                                    authenticate the prooving process.. Defaults to None.

        Returns:
            dict:signature
        """

        params = {"txid": tx_id, "addrerss": address}

        if message:
            params.update({"message": message})
        return self.__xcash_wallet_post(method="get_tx_proof", params=params)

    def check_tx_proof(self, tx_id: str, address: str, signature: str, message: str = None) -> dict:
        """Prove a transaction by checking its signature.‌

        Args:
            tx_id (str): transaction id.
            address (str): destination public address of the transaction.
            signature (str): transaction signature to confirm.
            message (str, optional):  Should be the same message used in get_tx_proof. Defaults to None.

        Returns:
            dict: _description_
        """
        params = {"txid": tx_id, "addrerss": address, "signature": signature}

        if message:
            params.update({"message": message})
        return self.__xcash_wallet_post(method="check_tx_proof", params=params)

    def get_spend_proof(self, tx_id: str, message: str = None) -> dict:
        """Generate a signature to prove a spend. Unlike proving a transaction, 
            it does not requires the destination public address.‌

        Args:
            tx_id (str):  transaction id.
            message (str, optional): add a message to the signature to further authenticate the prooving process.. Defaults to None.

        Returns:
            dict: spend signature.
        """
        params = {"txid": tx_id}

        if message:
            params.update({"message": message})
        return self.__xcash_wallet_post(method="get_spend_proof", params=params)

    def check_spend_proof(self, tx_id: str, signature: str, message: str = None) -> dict:
        """Prove a spend using a signature. Unlike proving a transaction, it does not requires 
        the destination public address.‌

        Args:
            tx_id (str): transaction id.
            signature (str): spend signature to confirm.
            message (str, optional): Should be the same message used in get_spend_proof. Defaults to None.

        Returns:
            dict: States if the inputs proves the spend.
        """
        params = {"txid": tx_id, "signature": signature}

        if message:
            params.update({"message": message})
        return self.__xcash_wallet_post(method="check_spend_proof", params=params)

    def get_reserve_proof(self, account_index: int, amount: int, all: bool = True, message: str = None) -> dict:
        """Generate a signature to prove of an available amount in a wallet.‌


        Args:
            account_index (int): Specify the account from witch to prove reserve. (ignored if all is set to true)
            amount (int): Amount (in atomic units) to prove the account has for reserve. (ignored if all is set to true)
            all (bool, optional): Proves all wallet balance to be disposable.. Defaults to True.
            message (str, optional): add a message to the signature to further authenticate the prooving process.. Defaults to None.

        Returns:
            dict: reserver signature
        """
        atomic = self.get_atomic(xcash_amount=amount)
        params = {"account_index": account_index, "amount": atomic, "all": all}

        if message:
            params.update({"message": message})
        return self.__xcash_wallet_post(method="get_reserve_proof", params=params)

    def check_reserve_proof(self, address: str, signature: str, message: str = None) -> dict:
        """Proves a wallet has a disposable reserve using a signature.‌


        Args:
            address (str): Public address of the wallet.
            signature (str): reserve signature to confirm.
            message (str, optional): Should be the same message used in get_reserve_proof. Defaults to None.

        Returns:
            dict:  good
        """

        params = {"address": address, "signature": signature}

        if message:
            params.update({"message": message})
        return self.__xcash_wallet_post(method="check_reserve_proof", params=params)

    def get_transfers(self, **kwargs) -> dict:
        """Returns a list of transfers.‌

        Kwargs: 
            in (bool, optional): Include incoming
            out (bool, optional): Include outgoing
            pending (bool, optional): Include pending
            failed (bool, optional): Include fails
            pool (bool, optional): Include in pool
            filter_by_height (bool, optional): Filter transfers by height
            min_height (int, optional): Minimum height to start query
            max_height (int, optional): Maximum block height to scan for transfers, if filtering by height is enabled (defaults to max block height).
            account_index (int, optional): Index of the account to query for transfers. (defaults to 0)
            subaddr_indices (list, optional): List of subaddress indices to query for transfers. (Defaults to empty - all indices)

        Returns:
            dict: out list, pending list, failed list, pool list
        """

        allowed = ["in", "out",'pending',"failed","pool","filter_by_height","min_height","max_height","account_index","subaddr_indices"]

        self.check_params(allowed_keys=allowed,params=kwargs )
        params={}
        if kwargs:
            params.update(kwargs)
        return self.__xcash_wallet_post(method="get_transfers", params=params)

    def get_tranfers_by_txid(self, tx_id: str, account_idex: int = 0) -> dict:
        """Show information about a transfer to/from this address.‌

        Args:
            tx_id (str): Transaction ID used to find the transfer.
            account_idex (int, optional): Index of the account to query for the transfer Defaults to 0.

        Returns:
            dict: transfer 
        """
        params = {"txid": tx_id, "account_index": account_idex}
        return self.__xcash_wallet_post(method="get_transfer_by_txid", params=params)

    def sign(self, data: str)-> dict:
        """Sign a string.‌

        Args:
            data (str): Anything you need to sign.
        Returns:
            dict: signature 
        """
        params = {"data": data}
        return self.__xcash_wallet_post(method="sign", params=params)

    def verify(self, data: str, address: str, signature: str) -> dict:
        """Verify a signature on a string.‌

        Args:
            data (str): What should have been signed.
            address (str): Public address of the wallet used to sign the data.
            signature (str): signature generated by sign method.

        Returns:
            dict: good
        """

        params = {"data": data, "address": address, "signature": signature}
        return self.__xcash_wallet_post(method="verify", params=params)

    def export_outputs(self) -> dict:
        """Export all outputs in hex format.‌

        Returns:
            dict: outputs_data_hex
        """
        return self.__xcash_wallet_post(method="export_outputs")

    def import_outputs(self, outputs_data_hex: str) -> dict:
        """Import outputs in hex format.‌

        Args:
            outputs_data_hex (str): num_imported; number of outputs imported.

        Returns:
            dict: num_imported  
        """
        return self.__xcash_wallet_post(method="import_outputs")

    def export_key_images(self) -> dict:
        """Export a signed set of key images.‌

        Returns:
            dict: signed_key_images 
        """
        return self.__xcash_wallet_post(method="export_key_images")

    def import_key_images(self, signed_key_images: list) -> dict:
        """Import signed key images list and verify their spent status.‌

        Args:
            signed_key_images (list): of  key_image, signature dict like structure

        Returns:
            dict: height, spent, unspent
        """
        params = {"signed_key_images": signed_key_images}
        return self.__xcash_wallet_post(method="import_key_images", params=params)

    def make_uri(self, address: str, **kwargs) -> dict:
        """Create a payment URI using the official URI spec.‌

        Args:
            address (str): Wallet address

        Kwargs: 
            amount (int, optional): the integer amount to receive, in atomic units
            payment_id (str, optional): 16 or 64 character hexadecimal payment id
            recipient_name ( str, optional): name of the payment recipient
            tx_descriptio n(str, optional): Description of the reason for the tx
        Returns:
            dict: uri
        """

        allowed = ["amount", "payment_id", "recipient_name", "tx_description"]
        self.check_params(allowed_keys=allowed, params=kwargs)
    
        params = {"address":address}
        if kwargs:
            params.update(kwargs)

        return self.__xcash_wallet_post(method="make_uri", params=params)

    def parse_uri(self, uri: str) -> dict:
        """Parse a payment URI to get payment information.‌

        Args:
            uri (str): This contains all the payment input information as a properly formatted payment URI

        Returns:
            dict: uri
        """

        return self.__xcash_wallet_post(method="parse_uri")

    def get_address_book(self, entries: list) -> dict:
        """Retrieves entries from the address book.‌

        Args:
            entries (list):  array of unsigned int; indices of the requested address book entries

        Returns:
            dict: : adddress
        """
        params = {"entries": entries}
        return self.__xcash_wallet_post(method="get_address_book", params=params)

    def add_address_book(self, address: str, payment_id: str = None, description: str = "") -> dict:
        """Add an entry to the address book.‌

        Args:
            address (str): XCASH valid address
            payment_id (str, optional): Payment ID. Defaults to None.
            description (str, optional): _description_. Defaults to "".

        Returns:
            dict: The index of the address book entry as INT
        """
        params = {"address": address, "description": description, "payment_id": payment_id}
        return self.__xcash_wallet_post(method="get_address_book", params=params)

    def delete_address_book(self, index: int) -> dict:
        """Delete an entry from the address book.

        Args:
            index (int): The index of the address book entry.

        Returns:
            dict: None
        """
        params = {"index": index}
        return self.__xcash_wallet_post(method="delete_address_book", params=params)

    def refresh_wallet(self, start_height: int=None) -> dict:
        """Refresh a wallet after openning.

        Args:
            start_height (int): The block height from which to start refreshing.

        Returns:
            dict: blocks_fetched, received_money
        """

        params = {"start_height": start_height}
        return self.__xcash_wallet_post(method="refresh", params=params)

    def rescan_spent(self) -> dict:
        """Rescan the blockchain for spent outputs.

        Returns:
            dict: _description_
        """
        return self.__xcash_wallet_post(method="rescan_spent")

    def get_languages(self) -> dict:
        """Rescan the blockchain for spent outputs.‌

        Returns:
            dict: languages
        """
        return self.__xcash_wallet_post(method="get_languages")

    def create_wallet(self, filename: str, password: str, language: str) -> dict:
        """Create a new wallet. You need to have set the argument "–wallet-dir" 
        when launching xcash-wallet-rpc to make this work.‌

        Args:
            filename (str): Wallet file name.
            password (str): password to protect the wallet.
            language (str): Language for your wallets' seed.

        Returns:
            dict: None
        """
        paramas = {"filename": filename, "password": password, "language": language}
        return self.__xcash_wallet_post(method="create_wallet", params=paramas)

    def open_wallet(self, filename: str, password: str) -> dict:
        """Open a wallet. You need to have set the argument "–wallet-dir" 
        when launching xcash-wallet-rpc to make this work.‌

        Args:
            filename (str): wallet name stored in –wallet-dir.
            password (str): only needed if the wallet has a password defined.

        Returns:
            dict: None
        """

        paramas = {"filename": filename, "password": password}
        return self.__xcash_wallet_post(method="open_wallet", params=paramas)

    def close_wallet(self) -> dict:
        """Close the currently opened wallet, after trying to save it.‌

        Returns:
            dict: None
        """
        return self.__xcash_wallet_post(method="close_wallet")

    def change_wallet_password(self, old_password: str, new_password: str) -> dict:
        """Change a wallet password.‌

        Args:
            old_password (str): Current wallet password, if defined.
            new_password (str): New wallet password, if not blank.

        Returns:
            dict: None
        """
        params = {"old_password": old_password, "new_password": new_password}
        return self.__xcash_wallet_post(method="change_wallet_password", params=params)

    def is_multisig(self) -> dict:
        """Check if a wallet is a multisig one.‌

        Returns:
            dict: multisig, ready, threshold, total
        """
        return self.__xcash_wallet_post(method="is_multisig")

    def prepare_multisig(self) -> dict:
        """Prepare a wallet for multisig by generating a multisig string to share with peers.‌

        Returns:
            dict: Multisig string to share with peers to create the multisig wallet.
        """
        return self.__xcash_wallet_post(method="prepare_multisig")

    def make_multisig(self, multisig_info: list, threshold: int, password: str) -> dict:
        """Make a wallet multisig by importing peers multisig string.‌

        Args:
            multisig_info (list): array of string; List of multisig string from peers.
            threshold (int): Amount of signatures needed to sign a transfer. Must be less or equal than
                 the amount of signature in multisig_info.
            password (str): Wallet password

        Returns:
            dict: address, multisig_info
        """
        params = {"multisig_info": multisig_info, "threshold": threshold, "password": password}
        return self.__xcash_wallet_post(method="make_multisig", params=params)

    def export_multisig_info(self) -> dict:
        """Export multisig info for other participants.‌

        Returns:
            dict: info
        """
        return self.__xcash_wallet_post(method="export_multisig_info")

    def import_multisig_info(self, info: list) -> dict:
        """Import multisig info from other participants.‌

        Args:
            info (list): List of multisig info in hex format from other participants.

        Returns:
            dict: n_outputs
        """
        params = {"info": info}
        return self.__xcash_wallet_post(method="import_multisig_info", params=params)

    def finalize_multisig(self, multisig_info: list, password: str) -> dict:
        """Turn this wallet into a multisig wallet, extra step for N-1/N wallets.

        Args:
            multisig_info (list): List of multisig string from peers.
            password (str): Wallet password

        Returns:
            dict: multisig wallet address.
        """
        params = {"multisig_info": multisig_info, "password": password}
        return self.__xcash_wallet_post(method="finalize_multisig", params=params)

    def sign_multisig(self, tx_data_hex: str) -> dict:
        """Sign a transaction in multisig.

        Args:
            tx_data_hex (str): Multisig transaction in hex format, as returned by transfer under multisig_txset.

        Returns:
            dict: tx_data_hex, tx_hash_list
        """
        params = {"tx_data_hex": tx_data_hex}
        return self.__xcash_wallet_post(method="sign_multisig", params=params)

    def submit_multisig(self, tx_data_hex: str) -> dict:
        """Submit a signed multisig transaction.

        Args:
            tx_data_hex (str): Multisig transaction in hex format, as returned by sign_multisig under tx_data_hex.

        Returns:
            dict: tx_hash_list
        """
        params = {"tx_data_hex": tx_data_hex}
        return self.__xcash_wallet_post(method="submit_multisig", params=params)

    def get_version(self) -> dict:
        """Get RPC version Major & Minor integer-format, where Major is the first 16 bits and Minor the last 16 bits.

        Returns:
            dict: RPC version, formatted with Major * 2^16 + Minor(Major encoded over the first 16 bits, 
                and Minor over the last 16 bits).
        """
        return self.__xcash_wallet_post(method="get_version")



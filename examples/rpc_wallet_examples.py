from xcash.rpc import XcashWalletRpc
from pprint import pprint

wallet = XcashWalletRpc()
# Get balance
balance = wallet.get_balance()
pprint(balance)

# Get address
address_data = wallet.get_address()
pprint(address_data)

# Get index of an address
second = "8BGpqditvSMPmezzAf86B2XHFFPMF3qmEZqtCwKxZZU1hi8fpvnzjgHFp4p3NLVcwgByQBGcoenQB7zEQe9VzMqxPLWmfpz"
index = wallet.get_address_index(address=second)
pprint(index)

# Create new address
new_address = wallet.create_address(label="Animus Private")
pprint(new_address)

# Label address
response = wallet.label_address(major=0, minor=1, label="Animus Private")
pprint(response)

# get all accounts
accounts = wallet.get_accounts()
pprint(accounts)

# Create account
response = wallet.create_account("Animus Private")
pprint(response)

# Label an account
label_response = wallet.label_account(account_index=1, label="Secondary")
pprint(label_response)

# Get account tags
account_tags = wallet.get_account_tags()
pprint(account_tags)

# Tag multiple accounts with same tag
tagging_result = wallet.tag_accounts(tag="Tag for account", accounts=[0])
pprint(tagging_result)

# Remove tags from accounts
untag_result = wallet.untag_accounts(accounts=[0])
pprint(untag_result)

# Set account tag description
description_result = wallet.set_account_tag_description(tag="Existing tag", description="This is the description")
pprint(description_result)

# Get wallet height
height = wallet.get_wallet_height()
pprint(height)

# Make a transfer
amount = 10.0  # Xcash
amount_atomic = wallet.get_atomic(
    xcash_amount=amount)  # Transfer requires atomic conversion of xcsah. Helper function can be used
addr = "XCA1kzoR3ZLNg5zxNmxrY8FYKtgEvPZqC2xoRpm1axCpQcrrZfoKTSkSNsASDspdt3j1WcEnQJyuuB5VPSB56WWy36A4sQtQhe"
dest = [{"amount": amount_atomic,  # format in atomic
         "address": addr}]

transfer_response = wallet.transfer(destinations=dest)
pprint(transfer_response)

# Make transfer split
amount = 10.0  # Xcash
amount_atomic = wallet.get_atomic(
    xcash_amount=amount)  # Transfer requires atomic conversion of xcsah. Helper function can be used
addr = "XCA1kzoR3ZLNg5zxNmxrY8FYKtgEvPZqC2xoRpm1axCpQcrrZfoKTSkSNsASDspdt3j1WcEnQJyuuB5VPSB56WWy36A4sQtQhe"
dest = [{"amount": amount_atomic,  # format in atomic
         "address": addr}]

transfer_response = wallet.transfer_split(destinations=dest)
pprint(transfer_response)

# Sign transfer
sign_response = wallet.sign_transfer(unsigned_txset="unsigned transaction set")
pprint(sign_response)

# Submit transfer
submit_response = wallet.submit_transfer(tx_data_hex="Transaction HEX data")
pprint(submit_response)

# Sweep Dust
sweep_response = wallet.sweep_dust()
pprint(sweep_response)

# Sweep all
address = "XCA....."
sweep_all_response = wallet.sweep_all(address=address)
pprint(sweep_all_response)

# Sweep single
destinations = [
    {
        "address": "Valid XCASH address",
        "amount": "atomic value of xcash as integer",  # For reference check transfer
    }
]
sweep_single = wallet.sweep_single(destinations=destinations)
pprint(sweep_single)

# Relay transaction
relay_result = wallet.relay_tx(hex='Hex string otransaction')
pprint(relay_result)

# Store wallet file
store_result = wallet.store()
pprint(store_result)

# Get payments by payment ID
payment_id = "0000000000000000000000000000000000000000000000000000000000000000"
payments = wallet.get_payments(payment_id=payment_id)

# Get bulk payments
payment_ids = ["0000000000000000000000000000000000000000000000000000000000000000"]
minimum_block_height = 120000
bulk_payments_result = wallet.get_bulk_payments(payment_ids=payment_ids, min_block_height=minimum_block_height)
pprint(bulk_payments_result)

# Get all incoming transfers
available_transfers = wallet.incoming_transfers(transfer_type="all")
pprint(available_transfers)

# Query by view key type
query_result = wallet.query_key(key_type="view_key")
pprint(query_result)

# Make integrated address
integrated_address = wallet.make_integrated_address()
pprint(integrated_address)

# Split integrated address
split_result = wallet.split_integrated_address(integrated_address="Integrated address required")
pprint(split_result)

# Stop wallet
stop_result = wallet.stop_wallet()
pprint(stop_result)

# Rescan blockchain
rescan = wallet.rescan_blockchain()
pprint(rescan)

# Set tx notes
tx_ids = ["f00426a332ab8eea7b0d8d219fd955b87debb49b1ff4d18d831bbe25426152e8"]
notes = ["This is an example"]
notes_result = wallet.set_tx_notes(tx_ids=tx_ids, notes=notes)
pprint(notes_result)

# Gwt tx notes
tx_ids = ["f00426a332ab8eea7b0d8d219fd955b87debb49b1ff4d18d831bbe25426152e8"]
get_notes_result = wallet.get_tx_notes(tx_ids=tx_ids)
pprint(get_notes_result)

# Set attributes
result = wallet.set_attribute(key="set", value="Attributed")
pprint(result)

# get attributes
result = wallet.get_attribute(key="set")
pprint(result)

# get tx keys
tx_id = "f00426a332ab8eea7b0d8d219fd955b87debb49b1ff4d18d831bbe25426152e8"
result = wallet.get_tx_key(tx_id=tx_id)
pprint(result)

# # Check tx keys
tx_id = "f00426a332ab8eea7b0d8d219fd955b87debb49b1ff4d18d831bbe25426152e8"
tx_key = "81ba662cf8fb6d0d0da18fc9b70ab28e01cc76311278fdd7fe7ab16360762b06"
addr = "XCA1kzoR3ZLNg5zxNmxrY8FYKtgEvPZqC2xoRpm1axCpQcrrZfoKTSkSNsASDspdt3j1WcEnQJyuuB5VPSB56WWy36A4sQtQhe"
result = wallet.check_tx_key(tx_id=tx_id, tx_key=tx_key, address=addr)
pprint(result)

# Get tx proof
tx_id = "f00426a332ab8eea7b0d8d219fd955b87debb49b1ff4d18d831bbe25426152e8"
addr = "XCA1kzoR3ZLNg5zxNmxrY8FYKtgEvPZqC2xoRpm1axCpQcrrZfoKTSkSNsASDspdt3j1WcEnQJyuuB5VPSB56WWy36A4sQtQhe"
result = wallet.get_tx_proof(tx_id=tx_id, address=addr)
pprint(result)

# Check tx proof
tx_id = "f00426a332ab8eea7b0d8d219fd955b87debb49b1ff4d18d831bbe25426152e8"
addr = "XCA1kzoR3ZLNg5zxNmxrY8FYKtgEvPZqC2xoRpm1axCpQcrrZfoKTSkSNsASDspdt3j1WcEnQJyuuB5VPSB56WWy36A4sQtQhe"
sig = "InProofV13vqBCT6dpSAXkypZmSEMPGVnNRFDX2vscUYeVS4WnSVnV5BwLs31T9q6Etfj9Wts6tAxSAS4gkMeSYzzLS7Gt4vvCSQRh9niGJMUDJsB5hTzb2XJiCkUzWkkcjLFBBRVD5QZ"
check_result = wallet.check_tx_proof(tx_id=tx_id, address=addr, signature=sig)

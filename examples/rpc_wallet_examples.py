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
pprint(check_result)

# Get reserve proof
tx_proof = wallet.get_reserve_proof()
pprint(tx_proof)

# Check reserve proof
reserve_address = "XCA1TzWy4E57dGZtVdciKsNV3rbAVTxgsEiH1bqv5aX3NNSVGavL2zUQN3k1i7pFifKFQ91ZtDjzf6TC7i6FwABA1Wr2ffSy6R"
signature = "ReserveProofV11BZ23sBt9sZJeGccf84mzyAmNCP3KzYbE1111112VKmH111118NwZ1xM1HTAd84ePcZSqFX6xBVieiDSoxYpCckL4DReogi9MTV113UXUtguEFV1zrU82oHgTV2eBjikYMnJEowkxibHPkk18K4Gye8tcr4u8ZBoTvdAV347nXpxxGjmUVvN7f9jnthihEETtjHWgP113kpYmq9tnad9iWuq79GzfaYSnCJwTSELA7ZYpovkgUTCGimj7eXR5JcC7tdrnFNT2yZyrvwdkhhU5f1QhYASkT8bEUjmm8FWMEfzPzq5A5pFFMdv8NQNYap7HZnQRCkxvEZUByvoDUUVoWSf9Fjnrs8tCyXh28yo3cjf8gg1SNtPXo6kohKwxNgaL1Ak9UAcoRJR7dGZtVdciKsNV3rbAVTxgsEiH1bqv5aX3NNSV6nnejGkeMJFg8VicB8CCAQDJ2rkUXiKwJsBuutypLEBu6frBYGmAVRSFt224VKfJfnVbx8M6k6Xq6Yu4pmcBJ4gZCDy"
proof_data = wallet.check_reserve_proof(address=reserve_address, signature=signature)
pprint(proof_data)

# Get transfers by minimum height
height = 800000
incoming_transfers = wallet.get_transfers(min_height=height)
pprint(incoming_transfers)

# Get transfers based on transaction ID
tx_id = "c36258a276018c3a4bc1f195a7fb530f50cd63a4fa765fb7c6f7f49fc051762a"
id_transfers = wallet.get_transfers_by_txid(tx_id=tx_id)
pprint(id_transfers)

# Sign a string
data_to_sing = "This is sample data to be signed"
signature = wallet.sign(data=data_to_sing)
pprint(signature)

# Verify a string
data_to_sing = "This is sample data to be signed"
address = "XCA1TzWy4E57dGZtVdciKsNV3rbAVTxgsEiH1bqv5aX3NNSVGavL2zUQN3k1i7pFifKFQ91ZtDjzf6TC7i6FwABA1Wr2ffSy6R"
signature = "SigV13jebbGm9a1H4PbfXd1SZyPPmRtnJAJaoyf6Q3pE1ABsCT1MmiG3VyALNYmHEnjYhx71Z5Yx2TQenjb18C3DKRkGz"
verification = wallet.verify(data=data_to_sing, address=address, signature=signature)
pprint(signature)

# Export outputs
outputs = wallet.export_outputs()
pprint(outputs)

# Import outputs
hex_data = "...outputs..."
import_result = wallet.import_outputs(outputs_data_hex=hex_data)

# Export key image
export_result = wallet.export_key_images()
pprint(export_result)

# Import key images
key_image = "f3174f34054d51c55e0c474cce70a38434a4674cfd425c9edaf94509b93e5848"
signature = "8ef6ce0f5267abd85021c3eeb18b5663fadd016ebdb0023c1657f2048fb1ed01d8d278cb1a71984c6ebe6fc053f46506c8267cfe19a1b5f1a3ee3dac89f7130b"
images_list = [{"key_image": "f3174f34054d51c55e0c474cce70a38434a4674cfd425c9edaf94509b93e5848",
                "signature": "8ef6ce0f5267abd85021c3eeb18b5663fadd016ebdb0023c1657f2048fb1ed01d8d278cb1a71984c6ebe6fc053f46506c8267cfe19a1b5f1a3ee3dac89f7130b"}]
import_data = wallet.import_key_images(signed_key_images=images_list)

# Make uri with amount and payment id
address = "XCA1TzWy4E57dGZtVdciKsNV3rbAVTxgsEiH1bqv5aX3NNSVGavL2zUQN3k1i7pFifKFQ91ZtDjzf6TC7i6FwABA1Wr2ffSy6R"
amount = 10
amount_atomic = wallet.get_atomic(amount)  # Convert the amount to atomic values so it can be processed
payment_id = "420fa29b2d9a49f5"
uri = wallet.make_uri(address=address, amount=amount_atomic, payment_id=payment_id)
pprint(uri)

# Parse Uri
uri_to_parse = ""
tx_data = wallet.parse_uri(uri=uri_to_parse)
pprint(tx_data)

# Get address book entries of first two addresses
addr_position = [0, 1]
entries = wallet.get_address_book(entries=addr_position)

# Add address to address book with address, payment id and description
address = "XCA1TzWy4E57dGZtVdciKsNV3rbAVTxgsEiH1bqv5aX3NNSVGavL2zUQN3k1i7pFifKFQ91ZtDjzf6TC7i6FwABA1Wr2ffSy6R"
payment_id = "420fa29b2d9a49f5"
description = "Third account"
add_result = wallet.add_address_book(address=address, payment_id=payment_id, description=description)
pprint(add_result)

# Delete address book
position = 1
result = wallet.delete_address_book(index=position)
pprint(result)

# Refresh wallet from height 800000
height = 800000
wallet.refresh_wallet(start_height=height)

# Rescan spent
wallet.rescan_spent()

# Get list of available languages
languages = wallet.get_languages()
pprint(languages)

# Create wallet with  name, password and English language

wallet_name = 'test'
password = "test123"
language = "English"
wallet_data = wallet.create_wallet(filename=wallet_name, password=password, language=language)
pprint(wallet_data)

# Open wallet
wallet_name = 'test'
password = "test123"
wallet.open_wallet(filename=wallet_name, password=password)

# Close wallet
wallet.close_wallet()

# change wallet password
old_password = "test123"
new_password = "123test"
result = wallet.change_wallet_password(old_password=old_password, new_password=new_password)
pprint(result)

# Is multisig
sig_result = wallet.is_multisig()
pprint(sig_result)

# Prepare multisig
multi_sig_info = wallet.prepare_multisig()
pprint(multi_sig_info)

# Export multisig info
multisig_info = wallet.export_multisig_info()
pprint(multisig_info)

# Make multisig for 2/2 Multisig Wallet:
multisig_info = [
    "MultisigV1K4tGGe8QirZdHgTYoBZMumSug97fdDyM3Z63M3ZY5VXvAdoZvx16HJzPCP4Rp2ABMKUqLD2a74ugMdBfrVpKt4BwD8qCL5aZLrsYWoHiA7JJwDESuhsC3eF8QC9UMvxLXEMsMVh16o98GnKRYz1HCKXrAEWfcrCHyz3bLW1Pdggyowop"]
threshold = 2
password = "test123"
multisig_data = wallet.make_multisig(multisig_info=multisig_info, threshold=threshold, password=password)
pprint(multisig_data)

# Import multisig
multsig_info = ["...multisig_info..."]
result = wallet.import_multisig_info(info=multisig_info)
pprint(result)

# Finalize multisig
multisig_info = [
    "MultisigxV1JNC6Ja2oBt5Sqea9LN2YEF7WYZCpHqr2EKvPG89Trf3X4E8RWkLaGRf29fJ3stU471MELKxwufNYeigP7LoE4tn2McPr4SbL9q15xNvZT5uwC9YRr7UwjXqSZHmTWN9PBuZEKVAQ4HPPyQciSCdNjgwsuFRBzrskMdMUwNMgKst1debYfm37i6PSzDoS2tk4kYTYj83kkAdR7kdshet1axQPd6HQ",
    "MultisigxV1Unma7Ko4zdd8Ps3Af4oZwtj2JdWKzwNfP6s2G9ZvXhMoSscwn5g7PyCfcBc1V4ffRHY3Kxqq6VocSCUTncpVeUskMcPr4SbL9q15xNvZT5uwC9YRr7UwjXqSZHmTWN9PBuZE1LTpWxLoC3vPMSrqVVcjnmL9LYfdCZz3fECjNZbCEDq3PHDiUuY5jurQTcNoGhDTio5WM9xaAdim9YByiS5KyqF4"]
password = "test123"
finalize_result = wallet.finalize_multisig(multisig_info=multisig_info, password=password)

# Sign multisig

hex_data = "...multisig_txset..."
sign_result = wallet.sign_multisig(tx_data_hex=hex_data)
pprint(sign_result)

# Submit multisig
hex_data = "...multisig_txset..."
submit_result = wallet.submit_multisig(tx_data_hex=hex_data)
pprint(submit_result)

# Get version
wallet_version = wallet.get_version()
pprint(wallet_version)

from pprint import pprint

from xcash.blockchainExplorer import BlockchainExplorer

blockchain = BlockchainExplorer()

# Blockchain data
data = blockchain.get_blockchain_data()
pprint(data)

# Circulating supply
supply = blockchain.get_circulating_supply()
pprint(supply)

# Current block height
current_block_height = blockchain.get_current_block_height()
pprint(current_block_height)

# Get generates supply
generates_supply = blockchain.get_generated_supply()
pprint(generates_supply)

# get last block data
last_block_data = blockchain.get_last_block_data()
pprint(last_block_data)

# get block data by hash or height
block_hash = "9ba4b59ea55b4131bbc6bd9ac7910e420436dd39373ff6ef7a498afca559b851"
block_height = 904075

block_data_by_hash = blockchain.get_block_data(block_data=block_hash)
pprint(block_data_by_hash)
block_data_by_height = blockchain.get_block_data(block_data=block_height)
pprint(block_data_by_height)

# Get transaction data
tx_hash = "None"  # Change None with transaction hash
tx_data = blockchain.get_transaction_data(tx_hash=tx_hash)
pprint(tx_data)

# Verify reserve proof
public_address = "None"
reserve_proof = "None"
data = None

proof_verification = blockchain.get_reserve_proof_verification(public_address=public_address,
                                                               reserve_proof=reserve_proof, data=data)
pprint(proof_verification)


# Generate integrated address
wallet_address = "XCA1kLpg7A9c919tsQZBDYPHoLSZgCzihZPgP569CtFpJvAvQrpqW72HZzLKHRRLpSQzpdKBwJeTaUXGco7E4tHr9TynMN5yfi"
generated_address = blockchain.generate_integrated_address(public_address=wallet_address)
pprint(generated_address)
